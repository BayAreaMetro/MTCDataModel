-- Draft --

# UrbanSim Buildings and Parcels

## Description  

**Buildings**  
The UrbanSim Buildings dataset includes attributes about the buildings on a parcel (e.g. year built, square footage, number of stories, use code).

**Parcels**
The Urbansim Parcels dataset includes parcel attributes (assessed date, land_improvement_ratio).

## Purpose and Use   
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research. More information about how these datasets are used can be found in the [Basemap section of the UrbanSim documentation](https://github.com/BayAreaMetro/petrale/blob/master/basemap/basemap_process.md).


## Data Processing   
These datasets are derived from the Parcel Regional Characteristics (PRC) and Parcels datasets.

- [PRC documentation](../land-people-mdm/parcel-characteristics.md)
- [Parcels documentation](../land-people-mdm/parcel-geometry.md)

**NOTE**: The links below are available internally at MTC only.

The figures below provides a high level overview of the subsequent data processing steps. 

**Figure 1. Data Processing Pre-Steps**
![Pre steps](https://www.lucidchart.com/publicSegments/view/986f91cf-cb8b-41d7-ae09-461ba80e3dfc/image.png)


**Figure 2. UrbanSim Tables Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/343a3c5c-af33-4f67-86b0-816a9cecb77c/image.png) 


- [Data Processing folder](https://github.com/BayAreaMetro/BASIS-Data-Processing/tree/master/urbansim/parcels_buildings)


## Field Definitions and Sources

[Field Documentation](https://mtcdrive.app.box.com/file/608892321712)


## Outputs

These datasets are available (internally at MTC) on Socrata:

- [Urbansim Buildings](https://data.bayareametro.gov/Cadastral/UrbanSim-Buildings-2018-v4a/a6kz-45xd)
- [Urbansim Parcels](https://data.bayareametro.gov/Cadastral/UrbanSim-Parcels-2018-v4a/nk3m-k4s8)

Join Field: **geom_id**


## Related Datasets

- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/qqfm-y9ey) | Join Field: geom_id
- [Parcel Grid 8 Mile](https://data.bayareametro.gov/dataset/Regional-Parcel-Grid-8-Mile/62ya-rtvu) | Join Field: geom_id
- [Parcel Grid Bridge Table]() | Join Field: geom_id (PK) -- Kearey to Add Later this week
- [UrbanSim Building Types](https://data.bayareametro.gov/Equivalencies/UrbanSim-Building-Types/a6fp-zvby) | Join Field: building_type


**Figure 3. Entity Relationship Diagram**

![UrbanSim Buildings and Parcels ERD](https://www.lucidchart.com/publicSegments/view/e4f8e610-8533-4acc-a926-17f34deb5560/image.png)


**Data Steward:** UrbanSim Team
