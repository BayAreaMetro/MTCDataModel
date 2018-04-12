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

### Environment

This documentation assumes the user is running MacOS or similar with GDAL 1.11.5 or >.   

#### Notes on GDAL Install. 

We use GDAL because it gracefully handles the types in the DBF files that these data are delivered in.  

You may already have gdal installed. You can check at the command line with:  

`ogr2ogr --version` 

You should see something like: `GDAL 1.11.5, released 2016/07/01`

If not, we recommend installing GDAL via [homebrew](https://brew.sh/):  

`brew install gdal`

### Download the source data. 

For convenience, these are organized into ISO files here:

- [MultiNet 2016 Source Data (MTC Staff Only)](https://s3-us-west-2.amazonaws.com/tomtomdisks/tomtom_mn_2016_12.iso)    
- [Local Points of Interest 2016 Source Data (MTC Staff Only)](https://s3-us-west-2.amazonaws.com/tomtomdisks/tomtom_lpoi_2016_12.iso)    

### Set up Files Up For Processing

Below we provide examples on how to set the files up. Please feel free to use, adapt, or use your own preferred method.

Copy the files off the disk after mounting it (in MacOS, double click on the ISO file).     

```
cp -R /Volumes/mn612ushd_ca_dvd1/nam2016_12/shpd/. ~/Data/tt16
cp -R /Volumes/lpo612ushd_ca_dvd1/nam2016_12/shpd/. ~/Data/tt16
cp -R /Volumes/mnap612ushd_ca_dvd1/nam2016_12/shpd/. ~/Data/tt16
```


Change permissions to allow file and folder changes in that directory. 

```
chmod -R ug+rw ~/Data/tt16
chmod -R ug+rw ~/Data/tt16
chmod -R ug+rw ~/Data/tt16
```

Move the files all into one directory (our script expects this).  

```
mv ~/Data/tt16/mn/usa/*/*.gz ~/Data/tt16/mn/usa
mv ~/Data/tt16/lpoi/usa/*/*.gz ~/Data/tt16/lpoi/usa
mv ~/Data/tt16/mnap/usa/*/*.gz ~/Data/tt16/lpoi/usa
```

Remove the (now empty) directories  

```
rm -rf ax tt16/mn/uc*
rm -rf ax tt16/mnap/uc*
rm -rf ax tt16/lpoi/uc*
```

Unzip all the files:

```
gunzip -r ~/Data/tt16/mn/usa
gunzip -r ~/Data/tt16/lpoi/usa
gunzip -r ~/Data/tt16/mnap/usa
```

### Merge all the tables and shapefiles from each region together.   

TomTom delivers the data partitioned by geographic regions that are not relevant to us. Therefore, we merge them all together. 

It might make sense to check whether the geographic partitions cross important boundaries (e.g. cities?) and if so, what happens to the shapes that cross those boundaries.

You can use the following script to scan the directory of prepped files and execute (or optionally export) the necessary bash scripts to merge the tables and shapefiles together, output them to a sqlite database, and (optionally) write them to a PostgreSQL database.   

For example, using [this script](https://github.com/BayAreaMetro/DataServices/blob/master/TomTom%20Base%20Map/etl/R/merge_tables.R)

## Outcomes

### Multinet 2016. 

#### Feature Counts and Metadata. 

See [here](https://github.com/BayAreaMetro/DataServices/blob/55e08ab3d0bb20df6252a2e48302ccab2850b62a/TomTom%20Base%20Map/etl/metadata/2016_multinet.csv)

#### Data. 

- [Spatial Data - GeoPackage (MTC Staff Only)](https://mtcdrive.box.com/s/u8rkmbnnzk2p8hn1knc8ek9e9ycccvxd). 
- [Spatial Data - SQL/PGDump (MTC Staff Only)](https://mtcdrive.box.com/s/qpxt802z2rv0k6fr5v2v3x571y312bqr)
- [Spatial Data - File Geodatabase (MTC Staff Only)](https://mtcdrive.box.com/s/qpxt802z2rv0k6fr5v2v3x571y312bqr).
- [Tables - SQLite3 (MTC Staff Only)](https://mtcdrive.box.com/s/42o3wmgwy4s3r8qav39b1pv4yomhrkhw). 
- [Tables - SQL/PGDump (MTC Staff Only)](https://mtcdrive.box.com/s/yn40apz8skg9os09bk49q7b4ld9xpj1a). 

### Local Points of Interest.
- In Progress. 

### Multinet 2017. 

These are some notes on thinking about the 2017 update. 

One key question is does the 2017 data have a spreadsheet with a list of layers like the one here:

https://github.com/BayAreaMetro/DataServices/blob/master/TomTom%20Base%20Map/etl/R/merge_tables.R#L12-L16

Another is: is the data from 2017 PSQL data?
