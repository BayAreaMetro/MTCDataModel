# Data Processing and Documentation  
  
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

1. Unzip all the shapefiles in the California Shapefiles DVD at the path 'nam2016_12\shpd\mn\usa\uc3' (this is what worked for 12/2016 data--may need to look into the rest of the paths (other parts of CA). Here's a [list](https://gist.github.com/tombuckley/2648c8fe9a776e2658d03a76769b07c4) of what the cryptic codes at the end of each file mean.  
2. Unzip all the metadata, which should be all files that end in *.xml.gz  
3. Create a list of all the shapefiles (df_sp)
4. Separate out the non-spatial tables (df)
4a. Review [2015_12 python script](https://github.com/BayAreaMetro/MTCDataModel/blob/master/TomTom%20Base%20Map/etl/2015_12_Processing.py)
5. Merge df and df_sp (`merge shapefiles.py` and `merge tables.py`)
6. Clean up files for load into DB (e.g. remove filenames starting with a number)
7. Make a fileGDB with the shapefiles `RegionalClipForDownload.py`

## Outcome

- A FileGDB with TomTom Geometries

## Results  

links to come   
