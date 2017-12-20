library(rgeos)
library(rgdal)
library(foreign)
library(dplyr)

#gunzip all tables in bash:
#gunzip -r 2016_12/
# Process Tables from mn product

path = "~/Documents/Projects/tomtom_tables/2016_12/nam2016_12/shpd/mn"

# Step 1. Turn myTables into a Dataframe with 3 columns c("Folder","Name","Type") Type= Shape or Table
myShapes <- list.files(path=path, pattern="*.shp", full.names=F, recursive=TRUE)
myTables <- list.files(path=path, pattern="*.dbf", full.names=F, recursive=TRUE)

myShapes2 <- gsub("___________","_", myShapes)
myShapes2 <- gsub("____","_", myShapes2)
myTables2 <- gsub("___________","_", myTables)
myTables2 <- gsub("____","_", myTables2)

tbl_df_temp <- strsplit(myTables2, "/|\\\\|\\.|_")
shp_df_temp <- strsplit(myShapes2, "/|\\\\|\\.|_")

#from https://stackoverflow.com/questions/4227223/r-list-to-data-frame
tbl_df1 <- data.frame(t(sapply(tbl_df_temp,c)))
shp_df1 <- data.frame(t(sapply(shp_df_temp,c)))

names(tbl_df1) <- c('folder1','folder2','shortname','file_ending')
names(shp_df1) <- c('folder1','folder2','shortname','file_ending')

tbl_df1['path'] <- myTables
shp_df1['path'] <- myShapes

library(dplyr)
non_spatial_tables <- anti_join(x = tbl_df1, y = shp_df1, by = c("folder1","folder2","shortname"))

# Step 2. Populate value for Type from myShapes

non_spatial_tables_grouped <- group_by(non_spatial_tables, shortname)

merge_files <- function(tbl1) {
  paths <- tbl1[['path']]
  shortname <- paste("/Users/tommtc/Box/DataViz\ Projects/Data\ Services/2016_12/TomTom2016/merged_tables/",tbl1[['shortname']][[1]],".dbf",sep="")
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
}

setwd(path)

non_spatial_tables_grouped %>% do(merge_files(.))

