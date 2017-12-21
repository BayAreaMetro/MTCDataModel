library(rgeos)
library(rgdal)
library(foreign)
library(dplyr)

####
#set up functions
####


merge_files <- function(tbl1,output_path,product) {
  paths <- tbl1[['path']]
  shortname <- paste(output_path,product,tbl1[['shortname']][[1]],".dbf",sep="")
  print("merging")
  print(shortname)
  for (currentFile in paths) {
    print(currentFile)
    if (!exists("dataset")){
      dataset <- read.dbf(currentFile, as.is = FALSE)
    }
    # if the merged dataset does exist, a??grou[ppend to it
    if (exists("dataset")){
      temp_dataset <-read.dbf(currentFile, as.is = FALSE)
      dataset<-rbind(dataset, temp_dataset)
      rm(temp_dataset)
    }
  }
  print("Writing to disk")
  print(shortname)
  write.dbf(file=shortname,dataset)
  return(data.frame())
}

merge_files_spatial <- function(tbl1, output_path, product) {
  paths <- tbl1[['path']]
  csv_shortname <- paste(output_path,product,
                         tbl1[['shortname']][[1]],
                         ".csv",sep="")
  shp_shortname <- paste("/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/merged_shapefiles/",
                         tbl1[['shortname']][[1]],
                         ".shp",sep="")
  print("merging")
  print(shp_shortname)
  for (currentFile in paths) {
    print(currentFile)
    if (!exists("dataset")){
      dataset <- st_read(currentFile)
      print("names")
      print(names(dataset))
    }
    # 
    if (exists("dataset")){
      temp_dataset <- st_read(currentFile)
      st_crs(temp_dataset) <- st_crs(dataset)
      print(names(dataset))
      dataset<-rbind(dataset, temp_dataset)
      rm(temp_dataset)
    }
  }
  print("Writing to disk")
  print(shp_shortname)
  st_write(dataset,shp_shortname)
  st_write(dataset,csv_shortname, 
           layer_options = "GEOMETRY=AS_WKT", 
           delete_dsn=TRUE)
  rowcount <- dims(dataset)[[1]]
  rm(dataset)
  return(rowcount)
}

walk_directory_and_merge_tables <- function(output_path,input_path, product_prefix, test=TRUE) {
  # Step 1. Turn myTables into a Dataframe with 3 columns c("Folder","Name","Type") Type= Shape or Table
  myShapes <- list.files(path=source_path, pattern="*.shp", full.names=F, recursive=TRUE)
  myTables <- list.files(path=source_path, pattern="*.dbf", full.names=F, recursive=TRUE)
  
  myShapes2 <- gsub("___________","_", myShapes)
  myShapes2 <- gsub("____","_", myShapes2)
  myTables2 <- gsub("___________","_", myTables)
  myTables2 <- gsub("____","_", myTables2)
  
  tbl_df_temp <- strsplit(myTables2, "/|\\\\|\\.|_")
  shp_df_temp <- strsplit(myShapes2, "/|\\\\|\\.|_")
  
  #from https://stackoverflow.com/questions/4227223/r-list-to-data-frame
  tbl_df1 <- data.frame(t(sapply(tbl_df_temp,c)))
  shp_df1 <- data.frame(t(sapply(shp_df_temp,c)))
  
  names(tbl_df1) <- c('folder1','product','shortname','file_ending')
  names(shp_df1) <- c('folder1','product','shortname','file_ending')
  
  tbl_df1['path'] <- myTables
  shp_df1['path'] <- myShapes
  
  non_spatial_tables <- anti_join(x = tbl_df1, y = shp_df1, by = c("folder1","product","shortname"))
  
  if (test==TRUE) {
    non_spatial_tables <- non_spatial_tables[2:3,]
  }
  
  non_spatial_tables_grouped <- group_by(non_spatial_tables, shortname)
  
  setwd(source_path)
  
  ####
  ###do the merge
  ####
  
  non_spatial_tables_grouped %>% do(merge_files(.data,output_path,product=product_prefix))
}

get_metrics_for_merged_tables <- function(output_path,input_path, product_prefix) {
  #add metrics:
  
  ## Metrics:
  # How many tables have no records?
  # 
  # at each table read: count of records
  # 
  # product, name of the features (feature class name), record, type(table/shape)
  # 
  # How many records are there in a previous release?
  # 
  # How many features are corrupt?
  
  merged_tables <- list.files(path=output_path, pattern="*.dbf", full.names=F, recursive=TRUE)
  
  merged_tables_tmp <- strsplit(merged_tables, "\\.")
  tbl_df2 <- data.frame(t(sapply(merged_tables_tmp,c)))
  shortnames <- tbl_df2[[1]]
  
  #get row count for merged tables
  setwd(output_path)
  rows <- c()
  for (filename in merged_tables) {
    df1 <- read.dbf(filename, as.is = FALSE)
    rowcount <- dim(df1)[[1]]
    rows <- append(rows, rowcount)
  }
  
  df_meta <- data.frame(filename=merged_tables,rowcount=rows,shortname=shortnames)
  
  setwd("~/Documents/Projects/DataServices/TomTom Base Map/etl")
  df_meta2 <- read_csv("metadata/2016_input_data_dictionary.csv")
  df_meta2['shortname'] <- sapply(df_meta2['abbrv'],FUN=tolower)
  df_meta3 <- inner_join(df_meta,df_meta2, by='shortname')
  df_meta4 <- df_meta3[,c('description','rowcount','feature_type','filename')]
  write_csv(df_meta4,paste(output_path,product_prefix,"table_names_and_row_counts.csv",sep=""))
}

####
## process lpoi
####

source_path = "~/Documents/Projects/tomtom_tables/2016_12/nam2016_12/shpd/lpoi"
output_path = "/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/lpoi/"

walk_directory_and_merge_tables(output_path, source_path,product_prefix="lpoi_", test=FALSE)
get_metrics_for_merged_tables(output_path, source_path,product_prefix="lpoi_")

######
##Process MN
####
#copied and pasted from above, should just put this all in a function

source_path = "~/Documents/Projects/tomtom_tables/2016_12/nam2016_12/shpd/mn"
output_path = "/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/multinet/"

walk_directory_and_merge_tables(output_path, source_path,product_prefix="mn_", test=FALSE)
get_metrics_for_merged_tables(output_path, source_path,product_prefix="mn_")

####
##Process mn spatial
####

input_path = "~/Documents/Projects/tomtom_tables/2016_12/"
output_path = "/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/mn/"
product="mn"

setwd(input_path)

df_shp_meta_tmp <- inner_join(shp_df1,df_meta2, by='shortname')

df_shp_meta <- df_shp_meta_tmp[,c('description','shortname','feature_type','path','merge_into')]

df_shp_meta$longname <- gsub(" ","_", df_shp_meta$description)

setwd("~/Documents/Projects/tomtom_tables/2016_12/nam2016_12/shpd/mn")

rows2 <- c()
df_shp_meta_grouped <- group_by(df_shp_meta, shortname)
rows2 <- append(rows2,df_shp_meta_grouped %>% do(merge_files_spatial(.data),output_path,product))

####
##Process poi spatial
####

input_path = "~/Documents/Projects/tomtom_tables/2016_12/"
output_path = "/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/mn/"
product="lpoi"

setwd(input_path)

df_shp_meta_tmp <- inner_join(shp_df1,df_meta2, by='shortname')

df_shp_meta <- df_shp_meta_tmp[,c('description','shortname','feature_type','path','merge_into')]

df_shp_meta$longname <- gsub(" ","_", df_shp_meta$description)

setwd("~/Documents/Projects/tomtom_tables/2016_12/nam2016_12/shpd/lpoi")

rows2 <- c()
df_shp_meta_grouped <- group_by(df_shp_meta, shortname)
rows2 <- append(rows2,df_shp_meta_grouped %>% do(merge_files_spatial(.data),output_path,product))


















