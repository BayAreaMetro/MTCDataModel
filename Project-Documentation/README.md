# Data Services: Project Documentation

## BASIS Master Data Management List
The following list contains the master data in use for the Bay Area Spatial Information System platform.  These datasets support all or part of MTC's Analytical Services, and drive decision making and policy development across the agency.  The data is grouped into five primary categories, and includes the following descriptive attributes:  

- Data Set Name
- Description
- Data Steward
- Data Source
- Date Added to MDM Inventory
- Update Frequency
- Date Last Published for Open use
- Publishing Status ()
- Sharing Permissions (Private/ Internal, Public/ External)
- Category (Policy, Transportation, Land & People, Administrative Boundaries, Environment)
- Subcategory
- Data Format
- Unit of Analysis (County, City, Zip, Tract, Block, Parcel, etc.)  

The figure below illustrates the details described above.
![MDM Detail](BASIS Master Data Management/images/dataset-detail.png) 

### The List (by Primary Category)
The list of all inventoried datasets can be found on the [BASIS Website](http://basis.bayareametro.gov/results)

#### Policy
Includes data on Growth Management, State & Federal Law, Regional Policies, Environmental Justice, Planning and Zoning Land Uses  

- [General Plan and Zoning 2018](https://mtc.data.socrata.com/Land-Use/General-Plan-and-Zoning-2018/udk3-z2d5) 
 | [Data Processing Notes](policy-mdm/regional-general-plan.md)

#### Transportation

##### Transit

[Regional Transit Database](https://github.com/MetropolitanTransportationCommission/RegionalTransitDatabase)   
Source: Transit Operators (via MTC 511)    
Input: [Google Transit Feed Specification](https://developers.google.com/transit/gtfs/) Text Files    
Output: Multiple, Bus Frequency by Geometry    
Dependencies: ~SQL Server~, Python, R, GDAL

- [Transit Stops]()  

- [Transit Lines]()  

#### Policy
- [Greenprint](redshift/greenprintFishnet.md) - Table structure for data acquired from Bay Area Greenprint
- [Priority Development Areas]()
- [Regional Land Uses](BASIS Master Data Management/readme.md)
- [Permit Geocode]()  

Note: Add the following sections to the data processing details for the residential housing permits data  

- [Housing Database Schema](hsngDBSchema.md) - Schemas for the tables comprising the housing database.
- [Entity Relation Diagram](https://bayareametro.github.io/DataServices/Project-Documentation/erd/housingDatabaseERD.pdf) - Diagram of views in the housing database.

#### TomTom Base Map
Documents and scripts for processing new TomTom Basemap data to create file geodatabases for distribution to Congestion Management Agencies and Transit Agencies in the San Francisco Bay Region.
  - [ETL](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/etl/)  
Extract Transform Load Scripts and documentation for the Tom Tom Basemap Datasets  

  - [PDFs](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/pdfs)  
Data Dictionary and UML Diagrams for Datasets.  

  - [Past Data Processing Documentation](https://bayareametro.github.io/DataServices/TomTom%20Base%20Map/pdfs/Procedures%20for%20Processing%20New%20TomTom%20Basemap%20Data.pdf)

