-- Draft --

# Department of Housing and Community Development (HCD)
## Housing Data 

From 2014-2017, MTC/ABAG underwent a process of collecting housing permit data from local jurisdictions based on their [Annual Progress Reports](https://www.hcd.ca.gov/community-development/housing-element/index.shtml). This was typically done via the use of a survey provided to jurisdictions, the results of which were then collated and analyzed to begin to provide a picture of housing production in the region. 

Based on these data, a housing portal website was developed to allow users to visualize these trends broken down by year, housing type and income category [Housing Data Portal](http://housing.abag.ca.gov)

Additionally, MTC used this housing permit data to inform it's [Housing Incentive Pool](https://mtc.ca.gov/our-work/fund-invest/investment-strategies-commitments/focused-growth/affordable-housing/housing) (HIP) grant program.

In 2018, HCD provided a platform for jurisdictions county-wide to directly submit APR information to them via a web portal. Entitlement and certificate of occupancy data were collected along with housing permit data. 

MTC now collects this housing data annually directly from HCD.




## Data Collection and Review Process
The data are provided by HCD as a single excel spreadsheet containing data for the region, exported from their database. The data include the following fields:

| Field Name                  | Field Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JURS_NAME                   | Name of jurisdiction submitting the report pursuant to Government Code 65400                                                                                    |
| CNTY_NAME                   | Name of the county that the jurisdiction is located in                                                                                                          |
| YEAR                        | Reporting year of the APR                                                                                                                                       |
| PRIOR_APN                   | Assessor's parcel number previously associated with the parcel, if applicable                                                                                   |
| APN                         | Current available Assessors parcel number the projected is located on                                                                                           |
| STREET_ADDRESS              | Number and name of the street the project is located on                                                                                                         |
| PROJECT_NAME                | Name of the project                                                                                                                                             |
| JURS_TRACKING_ID            | This may be the permit number or other identifier assigned by the reporting jurisdiction                                                                        |
| UNIT_CAT_DESC               | Unit Category Description                                                                                                                                       |
| TENURE                      | Tenure of project                                                                                                                                               |
| VLOW_INCOME_DR              | Number of units entitled - <br>very low-income, deed restricted                                                                                                 |
| VLOW_INCOME_NDR             | Number of units entitled - <br>very low-income, non deed restricted                                                                                             |
| LOW_INCOME_DR               | Number of units entitled - <br>low-income, deed restricted                                                                                                      |
| LOW_INCOME_NDR              | Number of units entitled - <br>low-income, non deed restricted                                                                                                  |
| MOD_INCOME_DR               | Number of units entitled - <br>moderate income, deed restricted                                                                                                 |
| MOD_INCOME_NDR              | Number of units entitled - <br>moderate income, non deed restricted                                                                                             |
| ABOVE_MOD_INCOME            | Number of units entitled - <br>above moderate income                                                                                                            |
| ENT_APPROVE_DT              | Date the entitlement was approved                                                                                                                               |
| NO_ENTITLEMENTS             | Total number of units issued entitlements in the project                                                                                                        |
| BP_VLOW_INCOME_DR           | Number of units issued building permits - <br>very low-income, deed   restricted                                                                                |
| BP_VLOW_INCOME_NDR          | Number of units issued building permits - <br>very low-income, non deed   restricted                                                                            |
| BP_LOW_INCOME_DR            | Number of units issued building permits - <br>low-income, deed restricted                                                                                       |
| BP_LOW_INCOME_NDR           | Number of units issued building permits - <br>low-income, non deed restricted                                                                                   |
| BP_MOD_INCOME_DR            | Number of units issued building permits - <br>moderate income, deed restricted                                                                                  |
| BP_MOD_INCOME_NDR           | Number of units issued building permits - <br>moderate income, non deed restricted                                                                              |
| BP_ABOVE_MOD_INCOME         | Number of units issued building permits - <br>above moderate income                                                                                             |
| BP_ISSUE_DT                 | Date the building permits were issued                                                                                                                           |
| NO_BILDING_PERMITS          | Total number of units issued building permits in the project                                                                                                    |
| CO_VLOW_INCOME_DR           | Number of units issued certificates of occupancy - <br>very low-income, deed   restricted                                                                       |
| CO_VLOW_INCOME_NDR          | Number of units issued certificates of occupancy - <br>very low-income, non   deed restricted                                                                   |
| CO_LOW_INCOME_DR            | Number of units issued certificates of occupancy - <br>low-income, deed   restricted                                                                            |
| CO_LOW_INCOME_NDR           | Number of units issued certificates of occupancy - <br>low-income, non deed   restricted                                                                        |
| CO_MOD_INCOME_DR            | Number of units issued certificates of occupancy - <br>moderate income, deed   restricted                                                                       |
| CO_MOD_INCOME_NDR           | Number of units issued certificates of occupancy - <br>moderate income, non   deed restricted                                                                   |
| CO_ABOVE_MOD_INCOME         | Number of units issued certificates of occupancy - <br>above moderate income                                                                                    |
| CO_ISSUE_DT                 | Date the certificates of occupancy or other form of readiness, <br>such as final inspection, was issued                                                         |
| NO_OTHER_FORMS_OF_READINESS | Total number of units that were issued certificates of occupancy or other forms of readiness                                                                    |
| EXTR_LOW_INCOME_UNITS       | Total number of units affordable to extremly low income residents                                                                                               |
| APPROVE_SB35                | Indicates if the project was approved using Government Code section 65913.4, <br>subdivision (b) (Streamlined Ministerial Approval Process (SB 35 Streamlining) |
| INFILL_UNITS                | Indicates if the project is considered "infill", per the definition described in the APR instructions                                                           |
| FIN_ASSIST_NAME             | Assistance programs used for each development <br>(required only for those projects with lower or moderate income, deed restricted units)                       |
| DR_TYPE                     | Indicates if the units are made affordable through a local policy or program, <br>such as inclusionary or denisty bonus ordinance                               |
| NO_FA_DR                    | Description of how the units were determined to be affordable without deed restrictions                                                                         |
| TERM_AFF_DR                 | How long the affordability term is                                                                                                                              |
| DEM_DES_UNITS               | Number of demolished or destroyed units associated with the new project                                                                                         |
| DEM_OR_DES_UNITS            | Indicates if the units were demolished or destroyed                                                                                                             |
| DEM_DES_UNITS_OWN_RENT      | Indicates of the demolished or destroyed units were owner or renter occupied                                                                                    |
| NOTES                       | Any notes included                                                                                                                                              |

## Data Processing
Once the data are received from HCD, MTC adds some additional fields that are required for internal analysis and in order to format the data for display in the housing portal. All fields added to the HCD dataset by MTC are prefaced with "MTC_".

The following is a list of fields that MTC adds to the HCD data, including what steps are necessary to calculate those fields where applicable. Fields are calculated based on total units for entitlements, permits and certificates being greater than one. In situations where multiple stages are issues in the same year, the most recent stage is used. For example, if an address has both a permit and certificate of occupancy issued in the same year, the address is added as a certificate of occupancy.

| Field Name               | Field Description                                         | Domain                                                                                        | Field Source | Type     | Calculation                                                                                                                                                                                            |
|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MTC_ID                   | Unique record identifier                                  |                                                                                               | MTC          | Text     |                                                                                                                                                                                                        |
|    <br>   MTC_YEAR       | Year issued                                               |                                                                                               | MTC          | Number   |                                                                                                                                                                                                        |
| MTC_ADDRESS_FULL         | Formatted Address                                         |                                                                                               | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_GEOCODE_ADDRESS      | Geocoded address                                          |                                                                                               | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_GEOCODE_TYPE         | Quality of geocoding                                      | ROOFTOP;<br>RANGE_INTERPOLATED;<br>GEOMETRIC_CENTER;<br>APPROXIMATE;<br>NOT_GEOCODED;<br>APN_MATCH     | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_WKT                  | Well known text representation of   geocoded location     |                                                                                               | MTC          | Point    |                                                                                                                                                                                                        |
| MTC_LONG                 | Longitude in decimal degress                              |                                                                                               | MTC          | Number   |                                                                                                                                                                                                        |
| MTC_LAT                  | Latitude in decimal degress                               |                                                                                               | MTC          | Number   |                                                                                                                                                                                                        |
| MTC_VLOW_TOT             | Sum of very low income units                              |                                                                                               | MTC          | Number   | Sum of VLOW_DR and VLOW_NDR                                                                                                                                                                            |
| MTC_LOW_TOT              | Low income total units                                    |                                                                                               | MTC          | Number   | Sum of LOW_DR and LOW_NDR                                                                                                                                                                              |
| MTC_MOD_TOT              | Number of units for moderate income                       |                                                                                               | MTC          | Number   | Sum of MOD_DR and MOD_NDR                                                                                                                                                                              |
| MTC_TOTAL_UNITS          | Total number of units for all income   levels             |                                                                                               | MTC          | Number   | Sum of All Income Categories (DR and NDR)                                                                                                                                                              |
| MTC_VLOW_INCOME_NDR      | Very low income units non-deed restricted                 |                                                                                               | MTC          | Number   | **IF** CO_VLOW_INCOME_NDR > 0, <br>**THEN** CO_VLOW_INCOME_NDR<br>**ELSE IF** BP_VLOW_INCOME_NDR<br>**THEN** BP_VLOW_INCOME_NDR<br>**ELSE IF** VLOW_INCOME_NDR > 0 <br>**THEN** VLOW_INCOME_NDR        |
| MTC_VLOW_INCOME_DR       | Very low income units deed restricted                     |                                                                                               | MTC          | Number   | **IF** CO_VLOW_INCOME_DR > 0, <br>**THEN** CO_VLOW_INCOME <br>**ELSE IF** BP_VLOW_INCOME_DR <br>**THEN** BP_VLOW_INCOME_DR<br>**ELSE IF** VLOW_INCOME_DR > 0 <br>**THEN** VLOW_INCOME_DR               |
| MTC_LOW_INCOME_NDR       | Low income units non-deed restricted                      |                                                                                               | MTC          | Number   | **IF** CO_LOW_INCOME_NDR > 0, <br>**THEN** CO_LOW_INCOME_NDR<br>**ELSE IF** BP_LOW_INCOME_NDR<br>**THEN** BP_LOW_INCOME_NDR<br>**ELSE IF** LOW_INCOME_NDR > 0 <br>**THEN** LOW_INCOME_NDR              |
| MTC_LOW_INCOME_DR        | Low income units deed restricted                          |                                                                                               | MTC          | Number   | **IF** CO_LOW_INCOME_DR > 0, <br>**THEN** CO_LOW_INCOME_DR<br>**ELSE IF** BP_LOW_INCOME_DR<br>**THEN** BP_LOW_INCOME_DR<br>**ELSE IF** LOW_INCOME_DR > 0 <br>**THEN** LOW_INCOME_DR                    |
| MTC_MOD_INCOME_NDR       | Number of units for moderate income   non-deed restricted |                                                                                               | MTC          | Number   | **IF** CO_MOD_INCOME_NDR > 0, <br>**THEN** CO_MOD_INCOME_NDR<br>**ELSE IF** BP_MOD_INCOME_NDR<br>**THEN** BP_MOD_INCOME_NDR<br>**ELSE IF** MOD_INCOME_NDRS > 0 <br>**THEN** MOD_INCOME_NDR             |
| MTC_MOD_INCOME_DR        | Number of units for moderate income deed   restricted     |                                                                                               | MTC          | Number   | **IF** CO_MOD_INCOME_DR > 0, <br>**THEN** CO_MOD_INCOME_DR<br>**ELSE IF** BP_MOD_INCOME_DR <br>**THEN** BP_MOD_INCOME_DR<br>**ELSE IF** MOD_INCOME_DR > 0 <br>**THEN** MOD_INCOME_DR                   |
| MTC_ABOVE_MOD_INCOME     | Above moderate income units                               |                                                                                               | MTC          | Number   | **IF** CO_ABOVE_MOD_INCOME > 0, <br>**THEN** CO_ABOVE_MOD_INCOME <br>**ELSE IF** BP_ABOVE_MOD_INCOME<br>**THEN** BP_ABOVE_MOD_INCOME<br>**ELSE IF** ABOVE_MOD_INCOME > 0 <br>**THEN** ABOVE_MOD_INCOME |
| MTC_ISSUE_DT             | Issue date                                                |                                                                                               | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_TYPE                 | Type of issue.                                            | ENTITLEMENT;<br>PERMIT;<br>CERTIFICATE                                                        | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_NOTES                | Additional MTC notes                                      |                                                                                               | MTC          | Text     |                                                                                                                                                                                                        |
| MTC_MAPPED               | Whether address has been geocoded   correctly or not      |                                                                                               | MTC          | Checkbox |                                                                                                                                                                                                        |
| MTC_PDA                  | Is point in a Priority Development Area?                  | TRUE;<br>FALSE                                                                                | MTC          | Checkbox |                                                                                                                                                                                                        |
| MTC_TPA                  | Is point in a Transit Priority Area?                      | TRUE;<br>FALSE                                                                                | MTC          | Checkbox |                                                                                                                                                                                                        |
| MTC_HOUSING_ELEMENT_SITE | Is address on a housing element site?                     | TRUE;<br>FALSE                                                                                | MTC          | Checkbox |                                                                                                                                                                                                        |

## Geocoding

Geocoding is conducted using Google's geocoding engine. Records that return a geocoding type of ROOFTOP or RANGE_INTERPOLATED are considered accurate for the needs of the internal spatial analysis. Records returning geocoding types of GEOMETRIC_CENTER or APPROXIMATE are reviewed and manually geocoded where possible. 

All records are also checked to make sure that they fall within the bounds of the 9 county Bay Area region. 
| Northeastern Lat/Long      | Southwestern Lat/Long       |
|----------------------------|-----------------------------|
| (38.864245,-121.208156)    | (36.893329,-123.632497)     |



## Spatial Analysis
Once geocoding is complete, all records are checked to see whether they fall inside Priority Development Areas, Transit Priority Areas and Housing Element Sites, and the appropriate fields (MTC_PDA, MTC_TPA, MTC_HOUSING_ELEMENT_SITE) are updated.

For 2018, these datasets were used:

[Priority Development Areas](https://opendata.mtc.ca.gov/datasets/priority-development-areas-plan-bay-area-2040)

[Transit Priority Areas](https://opendata.mtc.ca.gov/datasets/d97b4f72543a40b2b85d59ac085e01a0_0?geometry=-122.635%2C37.229%2C-121.482%2C37.420)

[Housing Element Sites](https://opendata.mtc.ca.gov/datasets/regional-housing-need-assessment-2015-2023-housing-element-sites?geometry=-122.410%2C37.801%2C-122.121%2C37.848)

