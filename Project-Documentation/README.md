# Data Services: Project Documentation

## Contents
### Enterprise Database Categories

### TomTom Base Map
Documents and scripts to create file geodatabases of base map data for California and the San Francisco Bay Region
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

[Priority Development Areas]()

### Projects

[Housing Permits]()
- [Permit Geocode]()
- [Housing Schema](hsngPermitSchema.md) - Schema containing housing permit (feature table and attribute table) and policy information for the region.

