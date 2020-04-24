--Draft--

# Parcel Regional Characteristics

### Description, Purpose, and Use
This documentation provides a high-level overview of the Parcel Regional Characteristics dataset. This dataset includes characteristics of the region's parcels including -- but not limited to -- land use, building characteristics, and monetary value. These characteristics are used in MTC/ABAG land use modeling, housing policy, and long range planning research. This dataset is the source of the UrbanSim Building and Parcels Datasets that are used for Plan Bay Area 2050's UrbanSim models.


#### Notable Dataset Caveats
- the parcel characteristics were collected from county assessors' offices in 2019, whereas the parcel geometries (denoted by the `joinid` field) were collected in 2018. Thus, there are parcels in this dataset without geometries (in cases where the APNs were new or different from the 2018 APNs)
- this dataset includes parcel characteristics as well as characteristics of the buildings on the parcels
- this data is minimally transformed from its source (from county assessors' offices), and is not suitable in this form for aggregation analyses
	- If you are interested in doing a parcel-based analysis using these parcel attributes, please send a request to the Data and Visualization team with your specifications


### Contents 

- [Data Collection](#data-collection)
- [Field Mapping and Documentation](#field-mapping-and-documentation)
- [Methodology](#methodology)
- [Outputs](#outputs)
- [Related Works](#related-works)


## Data Collection  
This dataset was compiled using parcel characteristics data from each of the nine counties' assessor's offices.


**NOTE**: The following links are internally at MTC only.

## Field Mapping and Documentation

### Field documentation

- [Alameda](https://mtcdrive.app.box.com/file/478745796177)
- [Contra Costa](https://mtcdrive.app.box.com/file/478747781665)
- [Marin](https://mtcdrive.app.box.com/file/478744669505)
- [Napa](https://mtcdrive.app.box.com/file/478750718724)
- [San Francisco](https://mtcdrive.app.box.com/file/478752103826)
- [San Mateo](https://mtcdrive.app.box.com/file/478760210577)
- [Santa Clara](https://mtcdrive.app.box.com/file/478766043565)
- [Solano](https://mtcdrive.app.box.com/file/478771812191)
- [Sonoma](https://mtcdrive.app.box.com/file/478765422296)

[**Field Mapping**](https://mtcdrive.app.box.com/file/562870529917)


## Methodology

**Figure 1.** Data Processing Overview

![Data Processing Diagram](https://www.lucidchart.com/publicSegments/view/cedfcb98-baf0-4946-849d-9a2861625378/image.png)

[**Data processing folder**](https://github.com/BayAreaMetro/BASIS-Data-Processing/tree/master/land-people/cadastral/parcel_regional_characteristics)


## Outputs

**NOTE**: Output tables available internally at MTC only.

[Parcel Regional Characteristics]()

**Derived Datasets:**

- [Urbansim Buildings]()
- [Urbansim Parcels]()


### Related Datasets

- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/qqfm-y9ey) | Join Field: `geom_id`
- [UrbanSim Building Types](https://data.bayareametro.gov/Equivalencies/UrbanSim-Building-Types/a6fp-zvby)  | Join Field: `building_type`

