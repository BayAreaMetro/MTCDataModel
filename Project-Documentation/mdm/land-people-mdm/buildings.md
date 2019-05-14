# Buildings  

## Description  
The parcel/building data includes the unique parcel identifier (APN) as well as attributes about the parcel (county, land value, if the parcel can’t be developed) and buildings (year assessed, square feet, number of stories, if the building is historic). Includes Historic and Commercial Bldgs. (basis)

## Purpose and Use   
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research. More information about how this dataset is used can be found in the [Basemap section of the UrbanSim documentation](https://github.com/BayAreaMetro/petrale/blob/master/basemap/basemap_process.md).

## Data Collection  
This data was compiled using local information collected from each of the 9 counties in the San Francisco Bay Area Region.  {Discuss Data Collection Effort Here}

## Data Processing   
This data is generated using a combination of sources and methods. The figure below provides a high level overview of the data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model](https://www.lucidchart.com/publicSegments/view/4325221a-7816-4525-a25e-d237b9b796f0/image.png) 


Field Mapping, Definitions, and Sources:

* **Alameda County**
   * [Alameda County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Alameda_Buildings_Field_Mapping.csv)
   * [Alameda County Assessor Field Documentation](https://mtcdrive.box.com/s/9nje22hvxgeri0pwb05dd4j0xrhr84mv)
* **Contra Costa County**
   * Contra Costa County Field Mapping **Not Currently Available**
   * Contra Costa County Assessor Field Documentation **Not Currently Available**
* **Marin County**
   * [Marin County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Marin_Buildings_Field_Mapping.csv)
   * [Marin County Assessor Field Documentation](https://mtcdrive.box.com/s/nahof8uz18qzqrl1i7zmzv7by0zqjslm)
* **Napa County**
   * [Napa County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Napa_Buildings_Field_Mapping.csv)
   * Napa County Assessor Field Documentaiton (**Not Currently Available**)
* **San Francisco County**
   * [San Francisco County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SF_Buildings_Field_Mapping.csv)
   * [San Francisco County Assessor Field Documentation](https://mtcdrive.box.com/s/8xyhr6uicc68be0boyqtv7fvcmun3mue)
* **San Mateo County**
   * [San Mateo County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SM_Buildings_Field_Mapping.csv)
   * [San Mateo County Assessor Field Documentation](https://mtcdrive.box.com/s/bai2l1erwum07rwk28dcsy05j4bcnpbo)
* **Santa Clara County**
   * [Santa Clara County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SC_Buildings_Field_Mapping.csv)
   * [Santa Clara County Assessor Field Documentation](https://mtcdrive.box.com/s/jd12binabjjnz7bigg50ajubgvgmj6do)
* **Solano County**
   * [Solano County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Solano_Buildings_Field_Mapping.csv)
   * [Solano County Assessor Field Documentation (**Not Currently Available**)
* **Sonoma County**
   * [Sonoma County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Sonoma_Buildings_Field_Mapping.csv)
   * [Sonoma County Assessor Field Documentation](https://mtcdrive.box.com/s/oi7065zrci2gu376f45yxa65n0fnwy9o)



## Entity Relationship Diagram and Attribute Definitions. 
The documentation and metadata details for this data can be viewed here: [Buildings 2018]() -- Socrata  

**Figure 2. Buildings Table Schema**  
![Buildings Table Schema](https://www.lucidchart.com/publicSegments/view/3c269e86-a479-4589-a807-18070db5e9be/image.png)  


**Note**:
Attribute Definitions can be viewed [Here]() -- Socrata

### Related Datasets

[Parcels 2018 Dataset](https://mtc.data.socrata.com/Cadastral/Region-Parcels-2018-/fqea-xb6g) | Join Field: joinid


Data Steward: UrbanSim Team
