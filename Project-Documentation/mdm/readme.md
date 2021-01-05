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

### [UrbanSim Datasets](urbansim-mdm)
Each of the following Datasets are related to the Assessor Parcel Records (Parcels 2018):  
- [Parcels](https://data.bayareametro.gov/Land-Use/UrbanSim-Parcels/6axv-s6xn) | [Documentation and Process Notes](urbansim-mdm/urbansim-buildings-parcels.md)
- [Buildings](https://data.bayareametro.gov/Land-Use/UrbanSim-Buildings/huqe-evqw) | [Documentation and Process Notes](urbansim-mdm/urbansim-buildings-parcels.md)
- [Build Out Capacity -- Previously Called PLU]() | [Documentation and Process Notes](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/urbansim-mdm/build-out-capacity.md) -- Not Yet Added to Inventory
- [Deed Restricted Units]() | [Documentation and Process Notes](urbansim-mdm/deed-restricted-units.md) -- Not Yet Added to Inventory
- [Development Pipeline]() | [Documentation and Process Notes](urbansim-mdm/development-pipeline.md)
- [Institutions]() | [Documentation and Process Notes](urbansim-mdm/institutions.md) -- Not Yet Added to Inventory
- [Landmarks]() | [Documentation and Process Notes](lurbansim-mdm/landmarks.md) -- Not Yet Added to Inventory
- [Nondevelopment Sites]() | [Documentation and Process Notes](urbansim-mdm/non-development-sites.md) -- Not Yet Added to Inventory


### Administrative Boundaries
- [LAFCO SOI Boundaries]() -- Not Yet Added to Inventory
- [Jurisdiction Boundaries]() -- Not Yet Added to Inventory
- [Urban Service Areas]() -- Not Yet Added to Inventory

### Environment  

#### Tabulation Layers
- [Greenprint](environment-mdm/greenprint-fishnet.md) | [Documentation and Process Notes](https://www.bayareagreenprint.org/glossary/)
Table structure for data acquired from Bay Area Greenprint

### [Policy](policy-mdm)
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
- [Priority Development Areas]() | [Documentation and Process Notes]()
- [Priority Production Areas]() | [Documentation and Process Notes]()
- [Priority Conservation Areas]() | [Documentation and Process Notes]()
- [Growth Geographies]() | [Documentation and Process Notes]()
- [Transit Priority Areas (Not Yet Added to Portal)]() | [Documentation and Process Notes](policy-mdm/regional-policies/transportation-priority-areas.md) 


### [Land & People](land-people-mdm)
Includes data that depicts local development, cadastral, buildings and structures and demography characteristics of local areas.

#### Cadastral

- [Parcel Regional Characteristics](https://data.bayareametro.gov/Cadastral/Parcel-Regional-Characteristics/8wj7-fdzw) | [Documentation and Process Notes](land-people-mdm/parcel-characteristics.md)
- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/fqea-xb6g) | [Documentation and Process Notes](land-people-mdm/parcel-geometry.md)
- [Parcels 2015]() -- Not Yet Added To Inventory
- [Parcels 2010]() -- Not Yet Added To Inventory


#### Housing
- [Residential Permits]() | [Data Processing Notes](land-people-mdm/residential-permits.md) -- Not Yet Added to Inventory

### [Transportation](transportation-mdm)
Includes data that depicts and describes the region's Transportation Systems

#### Transit

[Regional Transit Database](https://github.com/bayareametro/RegionalTransitDatabase)   
 
- [Transit Stops - Existing (2020)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=3faf8401623b48ae8d70f7a71d7365c9) | [Documentation and Process Notes](transportation-mdm/transit/transit-stops.md)
- [Transit Stops - Planned and Potential (2020)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=18a6239819b048fab9c87bb4d7649560) | [Documentation and Process Notes](transportation-mdm/transit/transit-stops.md) 
- [Transit Routes (2020)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=2a519083d0a44a33940e469e427c8457) | [Documentation and Process Notes (None Added)]()
- [Major Transit Stops (Not Yet Added to Portal)]() | [Documentation and Process Notes](transportation-mdm/transit/major-transit-stops.md)
