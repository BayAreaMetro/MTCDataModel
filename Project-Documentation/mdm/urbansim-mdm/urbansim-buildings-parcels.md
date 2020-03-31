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

The figures below provides a high level overview of the subsequent data processing steps. 

**Figure 1. Data Processing Pre-Steps**
![Pre steps](https://www.lucidchart.com/publicSegments/view/986f91cf-cb8b-41d7-ae09-461ba80e3dfc/image.png)


**Figure 2. UrbanSim Tables Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/5e742ffd-6888-42f2-aa3b-4a2488f3578e/image.png) 


[Process Notes](https://mtcdrive.app.box.com/notes/599518000054) (**NOTE**: Process notes available internally at MTC only)


### Field Definitions and Sources

[Field Documentation](https://mtcdrive.app.box.com/file/608892321712) (**NOTE**: Field documentation available internally at MTC only)


## Outputs

- [Urbansim Buildings]()
- [Urbansim Parcels]()


### Related Datasets

- [Parcels 2018]() | Join Field: geom_id
- [UrbanSim Building Types](https://data.bayareametro.gov/Equivalencies/UrbanSim-Building-Types/a6fp-zvby) | Join Field: building_type


**Figure 2. Entity Relationship Diagram**

![ERD](https://www.lucidchart.com/publicSegments/view/986f91cf-cb8b-41d7-ae09-461ba80e3dfc/image.png)


**Data Steward:** UrbanSim Team
