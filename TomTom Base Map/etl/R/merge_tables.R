tt_data_path <- file.path("~/Data/tt16/mn/usa")
prefix <- "tt_"

####
# Read the Metadata
####

library(readr)
library(readxl)
library(stringr)

shapefile_layers <- read_excel("~/Documents/Projects/DataServices/TomTom Base Map/etl/metadata/mapdoc_mn_gdf_3-6-6_vs_mn_shape_4-8_v1-0-1.xlsx",
                               sheet = "Shapefile Layers",
                               skip = 2,
                               col_types=c("text","text","text"),
                               col_names=c("abbrv","description","feature_type"))

#pad and lower abbreviations to match files
shapefile_layers$abbrv <- str_pad(shapefile_layers$abbrv, 2, pad="0")
shapefile_layers$abbrv <- str_to_lower(shapefile_layers$abbrv)
shapefile_layers$feature_type <- str_to_lower(shapefile_layers$feature_type)


#utility function
vector.is.empty <- function(x) return(length(x) ==0 )

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
##segment the files into tables
####

table_filenames <- shapefile_layers[with(shapefile_layers,
                                         feature_type == "table"),]$filenames
#drop nulls
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
#Move the merged tables to PostgreSQL
###
shortnames_pg <- sapply(first_tables, tt_parse, USE.NAMES=FALSE)
shortnames_pg <- paste0(prefix,shortnames)

local_pg <- "psql -U tom -d analysis_scratch -h 0.0.0.0"
schema_name <- "mn."
move_sqlite_to_pg <- paste0("ogr2ogr --config PG_USE_COPY YES -f PGDump ",
                            "-sql 'select * from ",
                            shortnames_pg,
                            "' /vsistdout/ -nln ",schema_name,
                            shortnames_pg, " db.sqlite ", "| PGPASSWORD=temp_pass ",
                            local_pg)




###
#Do the same for Shapefiles/GeoJSON/etc
#In this case writing back out to geojson
###
shape_filenames <- shapefile_layers[shapefile_layers$feature_type %in%
                                      c("point","line","polygon","area"),]$filenames
emptyv <- sapply(shape_filenames,vector.is.empty)
shape_filenames <- shape_filenames[!emptyv]

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

###GeoJSON--optional

first_geojson <- unlist(lapply(shape_filenames,function(x) x[1]))
shortnames <- sapply(first_geojson, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
create_geojson <- paste0("ogr2ogr -f 'GeoJSON' ",
                            shortnames, ".shp -nln ",
                            shortnames, " ", first_geojson)

other_geojson <- unlist(lapply(shape_filenames,function(x) x[2:length(x)]))
shortnames <- sapply(other_geojson, tt_parse, USE.NAMES=FALSE)
shortnames <- paste0(prefix,shortnames)
append_geojson <- paste0("ogr2ogr -f 'GeoJSON' ",
                            shortnames, ".shp -append -nln ",
                            shortnames, " ", other_geojson)

######
###
#Move the merged gpkg to PostGIS
###

###
#Special Treatment for Shapefile Polygons
###

shape_filenames_non_poly <- shapefile_layers[shapefile_layers$feature_type %in%
                                      c("point","line"),]$filenames
emptyv <- sapply(shape_filenames_non_poly,vector.is.empty)
shape_filenames_non_poly <- shape_filenames_non_poly[!emptyv]
first_non_poly <- unlist(lapply(shape_filenames_non_poly,function(x) x[1]))

shortnames_pgs <- sapply(first_non_poly, tt_parse, USE.NAMES=FALSE)
shortnames_pgs <- paste0(prefix,shortnames_pgs)

local_pg <- "psql -U tom -d analysis_scratch -h 0.0.0.0"
schema_name <- "mn_sp."
move_gpkg_to_pg_non_poly <- paste0("ogr2ogr --config PG_USE_COPY YES -f PGDump ",
                            "-sql 'select * from ",
                            shortnames_pgs,
                            "' /vsistdout/ -nln ",schema_name,
                            shortnames_pgs, " db.gpkg ", "| PGPASSWORD=temp_pass ",
                            local_pg)


shape_filenames_poly <- shapefile_layers[shapefile_layers$feature_type %in%
                                      c("area","polygon"),]$filenames
emptyv <- sapply(shape_filenames_poly,vector.is.empty)
shape_filenames_poly <- shape_filenames_poly[!emptyv]
first_poly <- unlist(lapply(shape_filenames_poly,function(x) x[1]))

shortnames_mpgs <- sapply(first_poly, tt_parse, USE.NAMES=FALSE)
shortnames_mpgs <- paste0(prefix,shortnames_mpgs)

move_gpkg_to_pg_poly <- paste0("ogr2ogr --config PG_USE_COPY YES -f PGDump ",
                            "-sql 'select * from ",
                            shortnames_mpgs,
                            "' /vsistdout/ -nlt PROMOTE_TO_MULTI -nln ",schema_name,
                            shortnames_mpgs, " db.gpkg ", "| PGPASSWORD=temp_pass ",
                            local_pg)


#######
##Move GeoPackage to FileGDB
######

emptyv <- sapply(shapefile_layers$filenames,vector.is.empty)
shapefile_layers_no_null_files <- shapefile_layers[!emptyv,]

shape_tablenames_non_poly <- shapefile_layers_no_null_files[shapefile_layers_no_null_files$feature_type %in%
											 	c("point","line","polygon","area"),]$abbrv


move_gpkg_to_filegdb_non_poly <- paste0("ogr2ogr ",
								   "-f FileGDB ",
								   "-append ",
								   "-sql 'select ST_MakeValid(geom) as geom, * from tt_",
								   shape_tablenames_non_poly,
								   "' -mapFieldType 'Integer64=Integer', db.gdb -nln tt_",
								   shape_tablenames_non_poly,
								   " db.gpkg")


###
#Execute the load for each table creation
###
#this requires an installation of GDAL
#optionally, uncomment to write to file and execute at shell
#write(create_tables, file="move_db_to_sqlite.sh")
setwd(tt_data_path)

results_create_tables <- sapply(create_tables, function(x) try(system(x,intern=TRUE)))

results_append_tables <- sapply(append_tables, function(x) try(system(x,intern=TRUE)))

results_move_sqlite_to_pg <- sapply(move_sqlite_to_pg[move_sqlite_to_pg], function(x) try(system(x,intern=TRUE)))

results_create_gpkg <- sapply(create_gpkg, function(x) try(system(x,intern=TRUE)))

results_append_gpkg <- sapply(append_gpkg[append_gpkg], function(x) try(system(x,intern=TRUE)))

results_move_gpkg_to_pg_non_poly <- sapply(move_gpkg_to_pg_non_poly, function(x) try(system(x,intern=TRUE)))

results_move_gpkg_to_pg_poly <- sapply(move_gpkg_to_pg_poly, function(x) try(system(x,intern=TRUE)))

results_create_geojson <- sapply(create_geojson, function(x) try(system(x,intern=TRUE)))

results_append_geojson <- sapply(append_geojson, function(x) try(system(x,intern=TRUE)))

system("ogr2ogr --long-usage")

#this command (writing to filegdb) requires a specific ogr2ogr install--
#specifically:
# brew unlink gdal
# brew tap osgeo/osgeo4mac && brew tap --repair
# brew install proj
# brew install geos
# brew install udunits
# brew install gdal2-filegdb
# brew link --force gdal2
#for some reason R's system command sees another GDAL install
#rather than debug the R environment, here we write out to a file to execute in shell/bash
#results_move_to_filegdb <- sapply(move_gpkg_to_filegdb_non_poly, function(x) try(system(x,intern=TRUE)))

write(move_gpkg_to_filegdb_non_poly, file="/Users/tommtc/Data/tt16/mn/usa/move_gpkg_to_filegdb_non_poly3.sh")


####also try it without makevalid
move_gpkg_to_filegdb <- paste0("ogr2ogr ",
								"-f FileGDB ",
								"-append -skipfailures ",
								"-sql 'select * from tt_",
								shape_tablenames_non_poly,
								"' -mapFieldType 'Integer64=Integer' db_not_makevalid.gdb -nln tt_",
								shape_tablenames_non_poly,
								" db.gpkg")

write(move_gpkg_to_filegdb, file="/Users/tommtc/Data/tt16/mn/usa/move_gpkg_to_filegdb_not_makevalid.sh")

