# Buildings

## Description
The parcel/building data includes the unique parcel identifier (APN) as well as attributes about the parcel (county, land value, if the parcel can’t be developed) and buildings (year assessed, square feet, number of stories, if the building is historic). Includes Historic and Commercial Bldgs. (basis)

## Purpose and Use  
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research.

## Data Collection
This data was compiled using local information collected from each of the 109 jurisdictions in the San Francisco Bay Area Region.  {Discuss Data Collection Effort Here}

## Data Processing
This data is generated using a combination of sources and methods (mainly Spatial Processing using MSSQL Spatial Queries). The figure below provides a high level overview of the data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model]() (Kaya)

## Entity Relationship Diagram and Attribute Definitions
The documentation and metadata details for this data can be viewed here: [Buildings 2018]() -- Socrata

**Figure 2. Entity Relationship Diagram**
![Land Use Data Model]()  


**Note**:
Attribute Definitions can be viewed [Here]() -- Socrata

This data is related to the [Parcels 2018 Dataset](https://mtc.data.socrata.com/Cadastral/Region-Parcels-2018-/fqea-xb6g) table using the joinid field.

Data Steward: UrbanSim Team
