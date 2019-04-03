# Institutions

## Description
Most of the information that goes into the land use forecast comes from the data in the basemap, the pipeline, and the forecast of market-rate development built by the UrbanSim Developer Model. However, large institutions often operate outside of the market, are unlikely to move, and are likely to expand operations at their current location. Examples of this include UC Berkeley, Cupertino City Hall, and Highland Hospital. Many of these entities also operate group quarters so all group quarter forecasting is also part of this database.

## Purpose and Use  
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research.

## Data Collection
This data was compiled using local information collected from each of the 109 jurisdictions in the San Francisco Bay Area Region.  {Discuss Data Collection Effort Here}

## Data Processing
This data is generated using a combination of sources and methods (mainly Spatial Processing using MSSQL Spatial Queries). The figure below provides a high level overview of the data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model]() -- Lucidcharts

## Entity Relationship Diagram and Attribute Definitions
The documentation and metadata details for this data can be viewed here: [Institutions 2018]() -- Socrata

**Figure 2. Entity Relationship Diagram**
![Land Use Data Model]() --Lucidcharts
Click [Here]() for interactive versions of Figures 1 and 2.

**Note**:
Attribute Definitions can be viewed [Here](). -- Socrata

This data is related to the [Parcels 2018 Dataset](https://mtc.data.socrata.com/Cadastral/Region-Parcels-2018-/fqea-xb6g) table using the joinid field.

Data Steward: UrbanSim Team