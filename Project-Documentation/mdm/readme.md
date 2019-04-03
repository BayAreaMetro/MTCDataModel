-- Draft --

# BASIS Master Data Management (MDM) Data Store
The following list identifies data that has been collected for the Bay Area Spatial Information System platform.  These datasets support MTC's Analytical Services and Long Range Planning efforts and drive decision making and policy development across the agency.  The data is managed by the Data & Visualization Team, with assistance from key staff that have been identified as Data Stewards in various units across the agency. Data is stored and managed within MTC's Enterprise Data Lake, and disseminated through the Socrata Connected Government Cloud Data as a Service (DaaS) Platform.  

The data is grouped into five primary categories, and includes the following descriptive attributes:  

- Data Set Name
- Description
- Data Steward
- Data Source
- Date Added to MDM Inventory
- Update Frequency
- Date Last Published for Open use
- Publishing Status
- Sharing Permissions (Private/ Internal, Public/ External)
- Category (Policy, Transportation, Land & People, Administrative Boundaries, Environment)
- Subcategory
- Data Format
- Unit of Analysis (County, City, Zip, Tract, Block, Parcel, etc.)  

The figure below illustrates the details described above.
![MDM Detail](../images/dataset-detail.png) 

The following list contains key datasets listed on the [BASIS Website](http://basis.bayareametro.gov/results) that have been marked for inclusion in the MDM Data Store.

### Administrative Boundaries
-- Not Yet Added To Inventory --
- [LAFCO SOI Boundaries](). -- Not Yet Added to Inventory
- [Jurisdiction Boundaries](). -- Not Yet Added to Inventory
- [Urban Service Areas](). -- Not Yet Added to Inventory

### Environment  

#### Tabulation Layers
- [Greenprint (Click to View)](redshift/greenprintFishnet.md) | [Data Processing Notes (Click to View)](https://www.bayareagreenprint.org/glossary/)
Table structure for data acquired from Bay Area Greenprint

### Policy
Includes data on Growth Management, State & Federal Law, Regional Policies, Environmental Justice, Planning and Zoning Land Uses.  

**Growth Management Boundaries and Policies**

- [Urban Growth Boundaries](policy-mdm/urban-growth-boundaries.md) | [Data Processing Notes (Click to View)](policy-mdm/urban-growth-boundaries.md) -- Not Yet Added to Inventory
    - Includes both Urban Limit Lines and Growth Management Areas (Parcel Based)

**Land Uses**

#### Potential Land Use (UrbanSim Team to Finalize Name and Document Processing Steps)
- [Zoning Lookup]() | [Data Processing Notes (Click to View)](policy-mdm/plu.md) -- Not Yet Added to Inventory

#### Existing (From Assessor Parcels/ DataViz to Document)

#### General Plan/ Zoning (From Local Jurisdictions) 
- [General Plan and Zoning 2018 (Click to View)](https://mtc.data.socrata.com/Land-Use/General-Plan-and-Zoning-2018/udk3-z2d5) 
 | [Data Processing Notes (Click to View)](policy-mdm/regional-general-plan.md)
 

#### Regional Policy Layers
- [Priority Development Areas (Parcel Based)]() -- Not Yet Added To Inventory
- [Transit Priority Areas (Parcel Based)]() -- Not Yet Added To Inventory  


### Land & People
Includes data that depicts local development, cadastral, buildings and structures and demography characteristics of local areas.

Each of the following Datasets are related to the Assessor Parcel Records (Parcels 2018):  
- [Buildings]() | [Data Processing Notes (Click to View)](land-people-mdm/buildings.md) -- Not Yet Added to Inventory
- [Deed Restricted Units]()  | [Data Processing Notes (Click to View)](land-people-mdm/deed-restricted-units.md) -- Not Yet Added to Inventory
- [Development Pipeline]()  | [Data Processing Notes (Click to View)](land-people-mdm/development-pipeline.md) -- Not Yet Added to Inventory
- [Institutions]()  | [Data Processing Notes (Click to View)](land-people-mdm/institutions.md) -- Not Yet Added to Inventory
- [Landmarks]()  | [Data Processing Notes (Click to View)](land-people-mdm/landmarks.md) -- Not Yet Added to Inventory
- [Nondevelopment Sites]()  | [Data Processing Notes (Click to View)](land-people-mdm/nondevelopmentsites.md) -- Not Yet Added to Inventory

#### Cadastral

- [Parcels 2018 (Click to View)](https://mtc.data.socrata.com/Cadastral/Region-Parcels-2018-/fqea-xb6g) | [Data Processing Notes (Click to View)]()
- [Parcels 2015]() -- Not Yet Added To Inventory
- [Parcels 2010]() -- Not Yet Added To Inventory

#### Housing
- [Residential Permits]()  | [Data Processing Notes (Click to View)](land-people-mdm/residential-permits.md) -- Not Yet Added to Inventory
Note: Add the following sections to the data processing details for the residential housing permits data  

### Transportation
Includes data that depicts and describes the region's Transportation Systems

#### Transit

[Regional Transit Database](https://github.com/bayareametro/RegionalTransitDatabase)   
Source: Transit Operators (via MTC 511)    
Input: [Google Transit Feed Specification](https://developers.google.com/transit/gtfs/) Text Files    
Output: Multiple, Bus Frequency by Geometry    
Dependencies: ~SQL Server~, Python, R, GDAL

- [Transit Stops]() -- Not Yet Added To Inventory  
- [Transit Lines]() -- Not Yet Added To Inventory  
