-- Draft --

# Urbansim Parcels  

## Description  
The Urbansim Parcels dataset includes the unique joinid, the county assessor's parcel number (APN), and parcel attributes (county, land value, if the parcel can’t be developed, etc.).

## Purpose and Use   
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research. More information about how this dataset is used can be found in the [Basemap section of the UrbanSim documentation](https://github.com/BayAreaMetro/petrale/blob/master/basemap/basemap_process.md).

## Data Collection  
This dataset was compiled using parcel characteristics data from each county's Assessor's Office.

## Data Processing   
This dataset is generated using a combination of sources and methods (Python, SQL, etc). Each county assessor's dataset is processed individually. The figure below provides a high level overview of the data processing steps. 

**Figure 1. Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/90c19317-b784-414e-9cb6-ff9e55d154b5/image.png) 


### Field Mapping, Definitions, and Sources

**NOTE**: Field documentation available internally at MTC only.

* **Alameda County**
   * [Alameda County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Alameda_Parcels_Field_Mapping.csv)
   * [Alameda County Assessor Field Documentation](https://mtcdrive.box.com/s/9nje22hvxgeri0pwb05dd4j0xrhr84mv)
* **Contra Costa County**
   * Contra Costa County Field Mapping (**Not Currently Available**)
   * Contra Costa County Assessor Field Documentation (**Not Currently Available**)
* **Marin County**
   * [Marin County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Marin_Parcels_Field_Mapping.csv)
   * [Marin County Assessor Field Documentation](https://mtcdrive.box.com/s/nahof8uz18qzqrl1i7zmzv7by0zqjslm)
* **Napa County**
   * [Napa County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Napa_Parcels_Field_Mapping.csv)
   * Napa County Assessor Field Documentaiton (**Not Currently Available**)
* **San Francisco County**
   * [San Francisco County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SF_Parcels_Field_Mapping.csv)
   * [San Francisco County Assessor Field Documentation](https://mtcdrive.box.com/s/8xyhr6uicc68be0boyqtv7fvcmun3mue)
* **San Mateo County**
   * [San Mateo County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SM_Parcels_Field_Mapping.csv)
   * [San Mateo County Assessor Field Documentation](https://mtcdrive.box.com/s/bai2l1erwum07rwk28dcsy05j4bcnpbo)
* **Santa Clara County**
   * [Santa Clara County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SC_Parcels_Field_Mapping.csv)
   * [Santa Clara County Assessor Field Documentation](https://mtcdrive.box.com/s/jd12binabjjnz7bigg50ajubgvgmj6do)
* **Solano County**
   * [Solano County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Solano_Parcels_Field_Mapping.csv)
   * [Solano County Assessor Field Documentation (**Not Currently Available**)
* **Sonoma County**
   * [Sonoma County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Sonoma_Parcels_Field_Mapping.csv)
   * [Sonoma County Assessor Field Documentation](https://mtcdrive.box.com/s/oi7065zrci2gu376f45yxa65n0fnwy9o)

## Entity Relationship Diagram and Attribute Definitions. 
The documentation and metadata for this dataset can be viewed here: [UrbanSim Parcels](https://data.bayareametro.gov/Cadastral/UrbanSim-Parcels/6q7r-gybw) -- Socrata  

**Figure 2. Urbansim Parcels Table Schema**   
![Urbansim Parcels](https://www.lucidchart.com/publicSegments/view/2e690d65-ee2c-4c3c-91b5-6286fa8d323e/image.png)


### Related Datasets

[Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/fqea-xb6g) | Join Field: joinid

[UrbanSim Buildings](https://data.bayareametro.gov/Structures/UrbanSim-Buildings/ahwz-jtst) | Join Field: joinid

Data Steward: UrbanSim Team
