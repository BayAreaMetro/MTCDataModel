-- Draft --

# UrbanSim Buildings and Parcels

## Description  

**Buildings**  
The UrbanSim Buildings dataset includes the unique building_id, the county assessor's parcel number (APN), as well as attributes about the buildings on the parcel (year built, square feet, number of stories, use code).

**Parcels**
The Urbansim Parcels dataset includes the unique joinid, the county assessor's parcel number (APN), and parcel attributes (county, assessed date, etc.).

## Purpose and Use   
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research. More information about how these datasets are used can be found in the [Basemap section of the UrbanSim documentation](https://github.com/BayAreaMetro/petrale/blob/master/basemap/basemap_process.md).


## Data Processing   
These datasets are subsets of the Parcel Regional Characteristics dataset ([documentation](parcel-characteristics.md)). The figure below provides a high level overview of the subsequent data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/4325221a-7816-4525-a25e-d237b9b796f0/image.png) 


### Field Mapping, Definitions, and Sources

**NOTE**: Field documentation available internally at MTC only.

![Urbansim table fields from Parcel Regional Characteristics](https://www.lucidchart.com/publicSegments/view/2e690d65-ee2c-4c3c-91b5-6286fa8d323e/image.png)


## Outputs

- [Urbansim Buildings](https://data.bayareametro.gov/Land-Use/UrbanSim-Buildings/huqe-evqw)
- [Urbansim Parcels](https://data.bayareametro.gov/Land-Use/UrbanSim-Parcels/6axv-s6xn)


### Related Datasets

- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/fqea-xb6g) | Join Field: Parcels 2018.joinid = parcel_id

- [Parcel Regional Characteristics](https://data.bayareametro.gov/Cadastral/Parcel-Regional-Characteristics/8wj7-fdzw) | Join Field: building_id


**Data Steward:** UrbanSim Team
