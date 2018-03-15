<a href="url"><img src="http://gis.mtc.ca.gov/mtcimages/mtcgisLogo.png" align="top" height="84" width="84" ></a>  

# TomTom Data
  
#### Table of Contents  
[Main Guide](#Main-Guide)   
[Detailed Guide](#Detailed-Guide)  
[Attributes](#Attributes)    
[Tables](#Tables)  
[Data](#Data)   

# Main Guide

MTC has a guide to using TomTom that is suitable to most users [here](http://gis.mtc.ca.gov/home/tomtom.html)

Users should consult that site first. Data there are organized by categories of use (e.g. Network, Base Map, Points of Interest) or by all data and are suitable for immediate use in Desktop Client applications (ESRI ArcMap, etc). 

# Detailed Guide

MTC Employees with specific needs or questions may want more detailed information. 

Based on work on the Extract, Transform, and Load process detailed [here](https://github.com/BayAreaMetro/DataServices/tree/master/TomTom%20Base%20Map/etl), we detail below a comprehensive list of the metadata for source data and their attributes. 

These data may be more suited to a user that wants to search for data by a specific attribute. They are not as refined but may still be useful.    

As a simple example, a user might search or scan the attribute list below for "Lanes", find the the table short-name it is associated with ("nw"), and then look up that data in the tables list ("Network"). 

If its a table, that table will be found in the sqlite database linked below. If its a point, line, or polygon, then it will be found in the file geodatabase linked below. Since network data are line data, they are found in the File Geodatabase below. 

The use case may be more complicated, and thats what this guide is oriented to. For example, we've found that [specific a request for features by TMC code](https://github.com/BayAreaMetro/vital-signs-traffic-data#table-names) was resolved using a process like this. 

In short, the goal below is to provide an overview of every attribute feature that is available without describing every relationship in the entire TomTom data model.

## Attributes

A comprehensive list of attributes across all tables is available [here](https://github.com/BayAreaMetro/DataServices/blob/master/TomTom%20Base%20Map/etl/metadata/attributes_by_table.md)

A sample of the table is below:

| Layer                                                                               | Field Name                                                                                                                   | Code | Name                                                       | Type |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------|------------------------------------------------------------|------|
| A0                                                                                  | MUNIT                                                                                                                        | 1F   | Unit of Measurement                                        | N    |
| OAO4                                                                                | ATTYP                                                                                                                        | 1G   | Military   Service Branch                                  | C    |
| LU                                                                                  | CLASS                                                                                                                        | 1H   | Classification                                             | N    |
| LU                                                                                  | IMPORT                                                                                                                       | 1I   | Park   Importance                                          | N    |
| LU                                                                                  | CLASS                                                                                                                        | 1J   | Park   Classification                                      | N    |
| RN                                                                                  | RTEPRIOR                                                                                                                     | 1K   | Route   Number Priority                                    | N    |
| RD                                                                                  | TMCPATHID                                                                                                                    | 1L   | TMC   Path ID                                              | N    |

## Tables

A list of the tables available in the TomTom data, their type (table, line, polygon) and the count of features in them is available [here](https://github.com/BayAreaMetro/DataServices/blob/master/TomTom%20Base%20Map/etl/metadata/2016_multinet.csv):

A sample of this table:

| abbrv | description                    | feature_type | layer_name | feature_count | 
|-------|--------------------------------|--------------|------------|---------------| 
| np    | Administrative Place Names     | table        | tt_np      | 1533          | 
| nw    | Network                        | line         | tt_nw      | 3429674       | 
| nwea  | Network Extended Attributes    | table        | tt_nwea    | 310774        | 
| oa01  | Census Tract (U.S. only)       | polygon      | tt_oa01    | 8057          | 
| oa02  | Census Block Group (U.S. only) | polygon      | tt_oa02    | 23212         | 
| oa03  | Census Blocks (U.S. only)      | polygon      | tt_oa03    | 697576        | 



## Data

### Desktop Client Usage (E.G. ESRI, R, Python, Javascript)
- [Spatial Data - File Geodatabase (MTC Staff Only)](https://mtcdrive.box.com/s/u8rkmbnnzk2p8hn1knc8ek9e9ycccvxd).
- [Tables - SQLite3 (MTC Staff Only)](https://mtcdrive.box.com/s/42o3wmgwy4s3r8qav39b1pv4yomhrkhw). 

### Database Usage:
- [Spatial Data - SQL/PGDump (MTC Staff Only)](https://mtcdrive.box.com/s/qpxt802z2rv0k6fr5v2v3x571y312bqr)
- [Tables - SQL/PGDump (MTC Staff Only)](https://mtcdrive.box.com/s/yn40apz8skg9os09bk49q7b4ld9xpj1a). 
