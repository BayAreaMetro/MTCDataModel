-- Draft --

# BASIS Master Data Management (MDM)
The following list identifies data that has been collected for the Bay Area Spatial Information System platform.  These datasets support MTC's Analytical Services and Long Range Planning efforts and drive decision making and policy development across the agency.  The data is managed by the Data & Visualization Team, with assistance from key staff that have been identified as Data Stewards in various units across the agency. Data is stored and managed within MTC's Enterprise Data Lake, and disseminated through the Socrata Connected Government Cloud Data as a Service (DaaS) Platform.  

The data is grouped into five primary categories, and includes the following descriptive attributes:  
![MDM Detail](../images/dataset-detail.png) 
The domain values for the list above include the following:
- Sharing Permissions Domains: Private/ Internal, Public/ External
- Category Domains: Policy, Transportation, Land & People, Administrative Boundaries, Environment
- Data Format Domains: Geographic, Tabular, Document
- Unit of Analysis Domains: County, City, Zip, Tract, Block, Parcel, etc.  

## Data Collection and Review Process
Most of the data that is collected for BASIS and included in the MDM has been identified for its usefulness when conducting policy based analytical work.  Much of the data comes from local jurisdictions in the nine county San Francisco Bay Area region, while a few datasets come from Federal, State or Local Agencies.  The following figure provides a high level overview of the BASIS Data Processing Flow.

**Figure 1. BASIS Data Processing Overview** 
![Data Processing Model](policy-mdm/images/dataset-processing.png)  

The following list contains key datasets listed on the [BASIS Website](http://basis.bayareametro.gov/results) that have been marked for inclusion in the MDM Data Store.

### UrbanSim Datasets   
Each of the following Datasets are related to the Assessor Parcel Records (Parcels 2018):  
- [Parcels](https://data.bayareametro.gov/Land-Use/UrbanSim-Parcels/6axv-s6xn) | [Documentation and Process Notes](land-people-mdm/urbansim-buildings-parcels.md)
- [Buildings](https://data.bayareametro.gov/Land-Use/UrbanSim-Buildings/huqe-evqw) | [Documentation and Process Notes](land-people-mdm/urbansim-buildings-parcels.md)
- [Build Out Capacity | Previously Called PLU]() | [Documentation and Process Notes]()
- [Deed Restricted Units]() | [Documentation and Process Notes](land-people-mdm/deed-restricted-units.md) -- Not Yet Added to Inventory
- [Development Pipeline]() | [Documentation and Process Notes](land-people-mdm/development-pipeline.md)
- [Institutions]() | [Documentation and Process Notes](land-people-mdm/institutions.md) -- Not Yet Added to Inventory
- [Landmarks]() | [Documentation and Process Notes](land-people-mdm/landmarks.md) -- Not Yet Added to Inventory
- [Nondevelopment Sites]() | [Documentation and Process Notes](land-people-mdm/non-development-sites.md) -- Not Yet Added to Inventory


### Administrative Boundaries
- [LAFCO SOI Boundaries]() -- Not Yet Added to Inventory
- [Jurisdiction Boundaries]() -- Not Yet Added to Inventory
- [Urban Service Areas]() -- Not Yet Added to Inventory

### Environment  

#### Tabulation Layers
- [Greenprint](redshift/greenprintFishnet.md) | [Documentation and Process Notes](https://www.bayareagreenprint.org/glossary/)
Table structure for data acquired from Bay Area Greenprint

### Policy
Includes data on Growth Management, State & Federal Law, Regional Policies, Environmental Justice, Planning and Zoning Land Uses.  

**Growth Management Boundaries and Policies**

- [Urban Growth Boundaries]() | [Documentation and Process Notes](policy-mdm/urban-growth-boundaries.md) -- Not Yet Added to Inventory
    - Includes both Urban Limit Lines and Growth Management Areas (Parcel Based)

**Land Uses**

#### Generalized Land Use (From Assessor Parcels/ DataViz to Document)
- [Generalized Land Use 2018]() | [Documentation and Process Notes](policy-mdm/land-use.md) -- Not Yet Added to Inventory

#### General Plan (From Local Jurisdictions) 
- [General Plan 2018](https://data.bayareametro.gov/Land-Use/View-of-Parcels-and-Regional-General-Plan-Codes-20/98c3-ikar) | [Documentation and Process Notes](policy-mdm/land-use.md)  

#### Zoning (From Local Jurisdictions)
- [Zoning 2018](https://data.bayareametro.gov/Land-Use/View-of-Parcels-and-Regional-Zoning-2018/q2p6-hbrp) | [Documentation and Process Notes](policy-mdm/land-use.md)

##### Master Land Use Lookup (For Use By Data Development Team Only)
- [General Plan and Zoning 2018](https://mtc.data.socrata.com/Land-Use/General-Plan-and-Zoning-2018/udk3-z2d5) 
 | [Documentation and Process Notes](policy-mdm/land-use.md)
 
 ##### UrbanSim Land Use
 - [Potential Land Use]() | [Documentation and Process Notes]()  
 
#### Regional Policy Layers
- [Priority Development Areas (Parcel Based)]() -- Not Yet Added To Inventory
- [Transit Priority Areas (Parcel Based)]() -- Not Yet Added To Inventory  


### Land & People
Includes data that depicts local development, cadastral, buildings and structures and demography characteristics of local areas.

#### Cadastral

- [Parcel Regional Characteristics](https://data.bayareametro.gov/Cadastral/Parcel-Regional-Characteristics/8wj7-fdzw) | [Documentation and Process Notes](land-people-mdm/parcel-characteristics.md)
- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/fqea-xb6g) | [Documentation and Process Notes](land-people-mdm/parcels_2018.md)
- [Parcels 2015]() -- Not Yet Added To Inventory
- [Parcels 2010]() -- Not Yet Added To Inventory


#### Housing
- [Residential Permits]() | [Data Processing Notes](land-people-mdm/residential-permits.md) -- Not Yet Added to Inventory

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
