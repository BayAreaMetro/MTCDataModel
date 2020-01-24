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
These datasets are derived from the Parcel Regional Characteristics dataset ([documentation](parcel-characteristics.md)). The figure below provides a high level overview of the subsequent data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/5e429cc2-8e0a-46c4-8046-333fa96aa474/image.png) 


### Field Mapping, Definitions, and Sources

**NOTE**: Field documentation available internally at MTC only.

![Urbansim table fields from Parcel Regional Characteristics](https://i.imgur.com/KfyM99n.png)


## Outputs

- [Urbansim Buildings](https://data.bayareametro.gov/UrbanSim/UrbanSim-Buildings-V1/wwij-t5vt)
- [Urbansim Parcels](https://data.bayareametro.gov/UrbanSim/UrbanSim-Parcels-V1/k3p6-mfvp)


### Related Datasets

- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018-geom_id/gnat-8ebd) | Join Field: geom_id
- [UrbanSim Building Types](https://data.bayareametro.gov/Equivalencies/UrbanSim-Building-Types/a6fp-zvby) | Join Field: building_type


**Figure 2. Entity Relationship Diagram**

![ERD](https://www.lucidchart.com/publicSegments/view/6e026cca-05a6-44e1-bb26-3abfd1604dfd/image.png)


**Data Steward:** UrbanSim Team
