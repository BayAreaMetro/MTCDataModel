# Data Services: Project Documentation

## Contents

### TomTom Base Map
Documents and scripts for processing new TomTom Basemap data to create file geodatabases for distribution to Congestion Management Agencies and Transit Agencies in the San Francisco Bay Region.
  - [ETL](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/etl/)  
Extract Transform Load Scripts and documentation for the Tom Tom Basemap Datasets  

  - [PDFs](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/pdfs)  
Data Dictionary and UML Diagrams for Datasets.  

  - [Past Data Processing Documentation](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/pdfs/Procedures%20for%20Processing%20New%20TomTom%20Basemap%20Data.pdf)
  
### Transportation

#### Transit

[Regional Transit Database](https://github.com/MetropolitanTransportationCommission/RegionalTransitDatabase)   
Source: Transit Operators (via MTC 511)    
Input: [Google Transit Feed Specification](https://developers.google.com/transit/gtfs/) Text Files    
Output: Multiple, Bus Frequency by Geometry    
Dependencies: ~SQL Server~, Python, R, GDAL

- [Transit Stops]()  

- [Transit Lines]()  

### Policy
- [Greenprint](redshift/greenprintFishnet.md) - Table structure for data acquired from Bay Area Greenprint
- [Priority Development Areas]()
#### BASIS Datasets
- [Potential Land Use](basis/plu_readme.md)

### Projects

#### Residential Building Permits <br/> 
- [Permit Geocode]()
- [Housing Database Schema](hsngDBSchema.md) - Schemas for the tables comprising the housing database.
- [Entity Relation Diagram](https://bayareametro.github.io/DataServices/Project-Documentation/erd/housingDatabaseERD.pdf) - Diagram of views in the housing database.

