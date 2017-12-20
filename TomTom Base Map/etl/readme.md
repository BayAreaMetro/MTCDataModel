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

[Tom Tom Dataset (MTC Staff Only)](https://mtcdrive.app.box.com/folder/35509938044)  

## Methodology

Pseudo-script based on [this detailed step by step doc](https://github.com/BayAreaMetro/MTCDataModel/blob/master/TomTom%20Base%20Map/pdfs/Procedures%20for%20Processing%20New%20TomTom%20Basemap%20Data.pdf):

1. Unzip all the shapefiles in the California Shapefiles DVD at the path 'nam2016_12\shpd:  

e.g. in bash: `find . -type f -name "*.gz" -exec gzip -d {} \;`  

3. Create a list of all the shapefiles 



4. Separate out the non-spatial tables 

4a. Review [2015_12 python script](https://github.com/BayAreaMetro/MTCDataModel/blob/master/TomTom%20Base%20Map/etl/2015_12_Processing.py)  

5. Merge df and df_sp (`merge shapefiles.py` and `merge tables.py`)  

6. Clean up files for load into DB (e.g. remove filenames starting with a number)  

7. Make a fileGDB with the shapefiles `RegionalClipForDownload.py`  

## Outcome

- A FileGDB with TomTom Geometries

## Results  

links to come   
