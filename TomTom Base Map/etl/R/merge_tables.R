##copy the files off the disk
#cp -R /Volumes/mn612ushd_ca_dvd1/nam2016_12/shpd/. ~/Data/tt16
##change permissions to allow file and folder changes in that directory
#chmod -R ug+rw ~/Data/tt16
##move them to one directory
#mv ~/Data/tt16/mn/usa/*/*.gz ~Data/tt16/mn/usa
##remove the (now empty) directories
#rm -rf ax uc*
##unzip all the files:
#gunzip -r .

tt_data_path <- file.path("~/Data/tt16/mn/usa")
prefix <- "tt_"

####
# Read the Metadata
####

library(readr)
library(readxl)
library(stringr)

shapefile_layers <- read_excel("~../metadata/mapdoc_mn_gdf_3-6-6_vs_mn_shape_4-8_v1-0-1.xlsx",
                               sheet = "Shapefile Layers",
                               skip = 2,
                               col_types=c("text","text","text"),
                               col_names=c("abbrv","description","feature_type"))

#pad and lower abbreviations to match files
shapefile_layers$abbrv <- str_pad(shapefile_layers$abbrv, 2, pad="0")
shapefile_layers$abbrv <- str_to_lower(shapefile_layers$abbrv)
shapefile_layers$feature_type <- str_to_lower(shapefile_layers$feature_type)

###
#define a function to get filenames for each shapefile layer
###
#' For a given abbreviation, return the filenames that correspond to it
#'
#' @param abbrv
#' @param feature_type
#' @param tt_data_path
#' @return vector of filenames
#' @examples
#' filenames <- tt_get_filenames(abbrv,feature_type,tt_data_path))
tt_get_filenames <- function(abbrv, feature_type, thepath) {
  if (feature_type=="table"){
    thepattern <- paste0("\\_",abbrv,".dbf")
    filenames <- list.files(path=thepath, pattern=thepattern, full.names=FALSE)
  } else
  {
    thepattern <- paste0("\\_",abbrv,".shp")
    filenames <- list.files(path=thepath, pattern=thepattern, full.names=FALSE)
  }
}

#' Parse a source filename and return its abbreviation.
#'
#'
#' @param filename a filename of some source data
#' @return the filename's abbreviated name
#' @examples
#' abbreviation <- abbrv('usauc5___________oa05.dbf.gz')
tt_parse <- function(filename) {
  filename <- gsub("usa", "", filename)
  filename <- gsub("gz", "", filename)
  v1 <- unlist(strsplit(filename, "\\.|_|___________|______________"))
  return(v1[2])
}

####
##apply the filename lookup function, returning filenames
####

shapefile_layers$filenames <- apply(shapefile_layers,1,
                                    function(x) tt_get_filenames(x['abbrv'],
                                                                 x['feature_type'],
                                                                 tt_data_path))

####
##segment the files into shapefiles
####

table_filenames <- shapefile_layers[with(shapefile_layers,
                                         feature_type == "table"),]$filenames
#drop nulls
vector.is.empty <- function(x) return(length(x) ==0 )
emptyv <- sapply(table_filenames,vector.is.empty)
table_filenames <- table_filenames[!emptyv]

###
#Prep the bash load script
#to load each first table
#here we write to sqlite
#because its easy to append to tables in it
#later we move these tables to postgres tt_data_pathectly
###
first_tables <- unlist(lapply(table_filenames,function(x) x[1]))
shortnames <- sapply(first_tables, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
create_tables <- paste("ogr2ogr -f ''SQLite'' db.sqlite -append -nln",
                       shortnames, first_tables)

######
###
#Prep the bash load script to append all other layers to first
###
other_tables <- unlist(lapply(table_filenames,function(x) x[2:length(x)]))
shortnames <- sapply(other_tables, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
append_tables <- paste("ogr2ogr -f ''SQLite'' db.sqlite -append -nln",
                       shortnames, other_tables)

######
###
#Move the merged tables to PostGIS
###
shortnames_pg <- sapply(first_tables, tt_parse, USE.NAMES=FALSE)
shortnames_pg <- paste0(prefix,shortnames)

local_pg <- "psql -U tom -d analysis_scratch -h 0.0.0.0"
schema_name <- "tt."
move_sqlite_to_pg <- paste0("ogr2ogr --config PG_USE_COPY YES -f PGDump ",
                            "-sql 'select * from ",
                            shortnames_pg,
                            "' /vsistdout/ -nln ",schema_name,
                            shortnames_pg, " db.sqlite ", "| PGPASSWORD=temp_pass ",
                            local_pg)

###
#Do the same for Shapefiles
#In this case writing back out to Shapefile
#Alternatively, write to GeoJSON, GeoPackage, tt_data_pathectly to PostGIS, etc
###
#shapefiles
shape_filenames <- shapefile_layers[shapefile_layers$feature_type %in%
                                      c("point","line","polygon","area"),]$filenames
emptyv <- sapply(shape_filenames,vector.is.empty)
shape_filenames <- shape_filenames[!emptyv]

first_shapefiles <- unlist(lapply(shape_filenames,function(x) x[1]))
shortnames <- sapply(first_shapefiles, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
create_shapefiles <- paste0("ogr2ogr -f 'ESRI Shapefile' ",
                            shortnames, ".shp -nln ",
                            shortnames, " ", first_shapefiles)

other_shapefiles <- unlist(lapply(shape_filenames,function(x) x[2:length(x)]))
shortnames <- sapply(other_shapefiles, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
append_shapefiles <- paste0("ogr2ogr -f 'ESRI Shapefile' ",
                            shortnames, ".shp -append -nln ",
                            shortnames, " ", other_shapefiles)

###prep output in other formats (shapefile 2gb max reached)
first_gpkg <- unlist(lapply(shape_filenames,function(x) x[1]))
shortnames <- sapply(first_gpkg, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
create_gpkg <- paste0("ogr2ogr -f 'GPKG' ",
                            "db.gpkg -append -nln ",
                            shortnames, " ", first_gpkg)

other_gpkg <- unlist(lapply(shape_filenames,function(x) x[2:length(x)]))
shortnames <- sapply(other_gpkg, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
append_gpkg <- paste0("ogr2ogr -f 'GPKG' ",
                            "db.gpkg -append -nln ",
                            shortnames, " ", other_gpkg)


###
#Execute the load for each table creation
###
#this requires an installation of GDAL
#optionally, uncomment to write to file and execute at shell
#write(create_tables, file="move_db_to_sqlite.sh")
setwd(tt_data_path)
results <- sapply(create_tables, function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded0 <- !vapply(results, is.error, logical(1))
print(table(succeeded0))
get.error.message <- function(x) {attr(x,"condition")$message}
message0 <- vapply(results[!succeeded0], get.error.message, "")

results <- sapply(append_tables, function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded1 <- !vapply(results, is.error, logical(1))
print(table(succeeded1))
get.error.message <- function(x) {attr(x,"condition")$message}
message1 <- vapply(results[!succeeded1], get.error.message, "")

results <- sapply(move_sqlite_to_pg[move_sqlite_to_pg], function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded2 <- !vapply(results, is.error, logical(1))
print(table(succeeded2))
get.error.message <- function(x) {attr(x,"condition")$message}
message2 <- vapply(results[!succeeded2], get.error.message, "")

results <- sapply(create_shapefiles, function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded3 <- !vapply(results, is.error, logical(1))
get.error.message <- function(x) {attr(x,"condition")$message}
message3 <- vapply(results[!succeeded3], get.error.message, "")

results <- sapply(append_shapefiles, function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded4 <- !vapply(results, is.error, logical(1))
get.error.message <- function(x) {attr(x,"condition")$message}
message4 <- vapply(results[!succeeded4], get.error.message, "")

results <- sapply(create_gpkg, function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded5 <- !vapply(results, is.error, logical(1))
get.error.message <- function(x) {attr(x,"condition")$message}
message3 <- vapply(results[!succeeded5], get.error.message, "")

results <- sapply(append_gpkg[append_gpkg], function(x) try(system(x)))
is.error <- function(x) inherits(x, "try-error")
succeeded6 <- !vapply(results, is.error, logical(1))
get.error.message <- function(x) {attr(x,"condition")$message}
message4 <- vapply(results[!succeeded6], get.error.message, "")
