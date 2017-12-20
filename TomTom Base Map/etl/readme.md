<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="84" width="84" ></a>  

# Tom Tom Data Processing and Documentation  
  
#### Table of Contents  
[Problem Statement](#problem-statement)   
[Data Sources](#data-sources)  
[Methodology](#methodology)   
[Expected Outcome](#outcome)  

## Problem Statement  

Make the source TomTom data accessible to various users at BayAreaMetro.  

## Data Sources

[Unzipped 2016 Tom Tom Dataset and Documentation (MTC Staff Only)](https://mtcdrive.app.box.com/folder/35509938044)  

## Environment

This documentation assumes the user is running MacOS or similar. 

Pseudo-script based on [this detailed step by step doc](https://github.com/BayAreaMetro/MTCDataModel/blob/master/TomTom%20Base%20Map/pdfs/Procedures%20for%20Processing%20New%20TomTom%20Basemap%20Data.pdf):

### Download the source data. 

For convenience, these are organized into zipfiles here:

- [2015 Source Data](https://mtcdrive.box.com/s/w5c4ofvh09uam2sornp2rc8nzo2r2i58)   
- [2016 Source Data](https://mtcdrive.box.com/s/b22pidd6h00zsbbkmadrkwsvmfea6uoq)    

### Unzip everything (twice)

After unzipping the downloaded zip file of choice, you need to unzip the tar.gz files for each source.

gunzip provides a useful recursive flag (`-r`): `gunzip -r 2016_12/`  

### Merge all the tables from each region together.   

For example, using this script: (MTCDataModel/blob/master/TomTom%20Base%20Map/etl/R/merge_tables.R

### Merge all the shapefiles from each region together.      

--Script forthcoming. 

### Output according to custom schema   

In the structure that is outlined in 2015 output schema: MTCDataModel/blob/master/TomTom%20Base%20Map/etl/metadata/2015_output_schema.json  

## Outcome

- A FileGDB with TomTom Geometries

## Results  

links to come   
