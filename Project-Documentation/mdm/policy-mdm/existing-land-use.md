-- Draft --

# Existing Land-Use 

## Description  
The Existing Land-Use dataset includes the unique rec_id, city_name, existing land use code (exlu_code), existing land use description (exlu_description), existing land use overlay (exlu_area_overlay), regional land use classification (regional_lu_class), minimum floor area ratio (min_far), maximum floor area ratio (max_far), minimum residential density (min_res), maximum residential density (max_res), editor name, edit_date, county_name, existing land use HEX color code (exlu_code_color).

## Purpose and Use   
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research. 

## Data Collection  
This dataset was compiled using APNs, Use_code, and usecode data from the Santa Clara county's Assessor's Office.

## Data Processing   
This data is generated using both AWS Redshift and MS-Excel. Data was sourced from Assessor then related to Use_code descriptions obtained from Assessor data documentation. The figure below provides a high level overview of the data processing steps.  

**Figure 1. Data Processing Steps**
![Data Processing Model]

### Field Mapping, Definitions, and Sources

**NOTE**: Field documentation available internally at MTC only.

* **Santa Clara County**
   * [Santa Clara County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SC_Buildings_Field_Mapping.csv)
   * [Santa Clara County Assessor Field Documentation](https://mtcdrive.box.com/s/jd12binabjjnz7bigg50ajubgvgmj6do)


## Entity Relationship Diagram and Attribute Definitions. 
The attribute documentation and metadata for this dataset can be viewed here: 

**Figure 2. Existing Land-Use Table Schema**  
[Existing Land-Use Table Schema]  

### Related Datasets
[Santa Clara County Assessor Documentation -> UseCodes for CHARACTERISTIC files.xls](https://mtcdrive.box.com/s/jd12binabjjnz7bigg50ajubgvgmj6do) | Join Field: Use_code

[Santa Clara County Assessor Dataset](https://mtcdrive.box.com/s/a31y6qyldh9xbtpn4cv9h6w8p03y8dh8) | Join Field: Use_code

Data Steward: DataViz Team
