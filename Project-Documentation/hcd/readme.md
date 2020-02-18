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

| Field source name              | Field description                                                            |
|--------------------------------|------------------------------------------------------------------------------|
| Entitlements                   |                                                                              |
| PRIOR_APN_CON_ENT_PERMITS      | Prior APN+                                                                   |
| APN_CON_ENT_PERMITS            | Current APN                                                                  |
| STREET_ADDRESS_CON_ENT_PERMITS | Street address                                                               |
| PROJECT_NAME_CON_ENT_PERMITS   | Project name                                                                 |
| JURS_TRACKIN_ID_CON_ENT_PERM   | Local jurisdiction tracking ID+                                              |
| UNIT_CAT_UID_CON_ENT_PERMITS   | Unit Category                                                                |
| TENURE_UID_CON_ENT_PERMITS     | Tenure (770=Owner, 769=Renter)                                               |
| VLOW_INCOME_DR_CON_ENT_PERMITS | Very Low Income Deed Restricted                                              |
| VLOW_INCOME_NDR_CON_ENT_PERM   | Very Low Income Non Deed Restricted                                          |
| LOW_INCOME_DR_CON_ENT_PERMITS  | Low Income Deed Restricted                                                   |
| LOW_INCOME_NDR_CON_ENT_PERMITS | Low Income Non Deed Restricted                                               |
| MOD_INCOME_NDR_CON_ENT_PERMITS | Moderate Income Non Deed Restricted                                          |
| ABOVE_MOD_INCOME_CON_ENT_PERM  | Above Moderate Income                                                        |
| ENT_APPROVE_DT_CON_ENT_PERMITS | Date of Approved Entitlement                                                 |
| NO_OF_UNITS_ISSUED_ENT         | Number Of Units With Entitlements Issued                                     |
| Building Permits               |                                                                              |
| BP_VLOW_INCOME_DR_CON_ENT_PERM | Very low-income deed restricted                                              |
| BP_VLOW_INCOME_NDR_CON_PERM    | Very low-income non deed restricted                                          |
| BP_LOW_INCOME_DR_CON_ENT_PERM  | Low-income deed restricted                                                   |
| BP_LOW_INCOME_NDR_CON_ENT_PERM | Low-income non deed restricted                                               |
| BP_MOD_INCOME_DR_CON_ENT_PERM  | Moderate-income deed restricted                                              |
| BP_MOD_INCOME_NDR_CON_ENT_PERM | Moderate-income non deed restricted                                          |
| BP_ISSUE_DT_CON_ENT_PERM       | Building permit issue date                                                   |
| NO_OF_UNITS_ISSUED_BLD_PERMITS | Number of units issued building permits                                      |
| Certificates of Occupancy      |                                                                              |
| CO_VLOW_INCOME_DR_CON_ENT_PERM | Very low-income deed restricted                                              |
| CO_MOD_INCOME_NDR_CON_ENT_PERM | Moderate-income non deed restricted                                          |
| CO_LOW_INCOME_DR_CON_ENT_PERM  | Low-income deed restricted                                                   |
| CO_LOW_INCOME_NDR_CON_ENT_PERM | Low-income non deed restricted                                               |
| CO_ISSUE_DT_CON_ENT_PERM       | Certificate of occupancy issue date                                          |
| NO_OF_U_ISS_CERTI_READINESS    | Number of units issued certificates of occupancy or other forms of readiness |
| Additional data                |                                                                              |
| EXTR_LOW_INCOME_UNITS_CON_PERM | Extra Low Income Units                                                       |
| APPROVE_SB35_CON_ENT_PERM      | Was Project APPROVED Using GC 65913.4(b)?  (SB 35 Streamlining) Y/N          |
| INFILL_UNITS_CON_ENT_PERM      | Infill Units                                                                 |
| FIN_ASSIST_DETAIL              | Financial Assistance Detail                                                  |
| DR_TYPE_CON_ENT_PERM           | Deed Restriction Type                                                        |
| NO_FA_DR_CON_ENT_PERM          | No Financial Assistance Deed Restricted                                      |
| TERM_AFF_DR_CON_ENT_PERM       | Term of Affordability or Deed Restriction                                    |
| DEM_DES_UNITS_CON_ENT_PERM     | Number of Demolished/Destroyed Units                                         |
| DEM_OR_DES_UNITS_CON_ENT_PERM  | Demolished or Destroyed Units                                                |
| DEM_DES_UNITS_OWN_RENT_CON_P   | Demolished/Destroyed Units Owner Or Renter                                   |
| NOTES_CON_ENT_PERM             | Notes+                                                                       |
| ACQUISITION_DESC_ACTIVITY      | Acquisition description activity                                             |
| ACQUISITION_ELOW_INCOME        | Units acquired, extremely low-income                                         |
| ACQUISITION_LOW_INCOME         | Units acquired, low-income                                                   |
| ACQUISITION_VLOW_INCOME        | Units acquired, very low-income                                              |
| PRESERVE_DESC_ACTIVITY         | Preservation description activity                                            |
| PRESERVE_ELOW_INCOME           | Units preserved, extremely low-income                                        |
| PRESERVE_LOW_INCOME            | Units preserved, low-income                                                  |
| PRESERVE_VLOW_INCOME           | Units preserved, very-low income                                             |
| REHAB_DESC_ACTIVITY            | Rehabiliation description activity                                           |
| REHAB_ELOW_INCOME              | Units rehabilitated, extremely low-income                                    |
| REHAB_LOW_INCOME               | Units rehabilitated, low-income                                              |
| REHAB_VLOW_ INCOME             | Units rehabilitated, very low-income                                         |

## Data Processing
Once the data are received from HCD, MTC adds some additional fields that are required for internal analysis and in order to format the data for display in the housing portal. All fields added to the HCD dataset by MTC are prefaced with "MTC_".

The following is a list of fields that MTC adds to the HCD data, including what steps are necessary to calculate those fields where applicable. Fields are calculated based on total units for entitlements, permits and certificates being greater than one. In situations where multiple stages are issues in the same year, the most recent stage is used. For example, if an address has both a permit and certificate of occupancy issued in the same year, the address is added as a certificate of occupancy.

| Field Name               | Field Description                                               | Type       | Calculation                                                                                                                                                                                                                                     |
|--------------------------|-----------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MTC_YEAR                 | Year issued                                                     | Number     |                                                                                                                                                                                                                                                 |
| MTC_WKT                  | Well known text representation of geocoded location             | Point      |                                                                                                                                                                                                                                                 |
| MTC_VLOW_TOT             | Sum of very low income units                                    | Number     | Sum of VLOW_DR and VLOW_NDR                                                                                                                                                                                                                     |
| MTC_VLOW_INCOME_NDR      | Very low income units non-deed restricted                       | Number     | IF CO_VLOW_INCOME_NDR_CON_ENT_PERM > 0, THEN CO_VLOW_INCOME_NDR_CON_ENT_PERM ELSE IF BP_VLOW_INCOME_NDR_CON_ENT_PERM THEN BP_VLOW_INCOME_NDR_CON_ENT_PERMELSE IF VLOW_INCOME_NDR_CON_ENT_PERMITS > 0 THEN VLOW_INCOME_NDR_CON_ENT_PERMITS       |
| MTC_VLOW_INCOME_DR       | Very low income units deed restricted                           | Number     | IF CO_VLOW_INCOME_DR_CON_ENT_PERM > 0, THEN CO_VLOW_INCOME_DR_CON_ENT_PERM ELSE IF BP_VLOW_INCOME_DR_CON_ENT_PERM THEN BP_VLOW_INCOME_DR_CON_ENT_PERMELSE IF VLOW_INCOME_DR_CON_ENT_PERMITS > 0 THEN VLOW_INCOME_DR_CON_ENT_PERMITS             |
| MTC_TYPE                 | Type of issue. Entitlement, Permit or Certificate of Occupancy  | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_TPA                  | Is point in a Transit Priority Area?                            | Checkbox   |                                                                                                                                                                                                                                                 |
| MTC_TOTAL_UNITS          | Total number of units for all income levels                     | Number     | Sum of All Income Categories (DR and NDR)                                                                                                                                                                                                       |
| MTC_PDA                  | Is point in a Priority Development Area                         | Checkbox   |                                                                                                                                                                                                                                                 |
| MTC_NOTES                | Additional MTC notes                                            | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_NO_OF_UNITS          | Total number of units for all income levels                     | Number     |                                                                                                                                                                                                                                                 |
| MTC_MOD_TOT              | Number of units for moderate income                             | Number     | Sum of MOD_DR and MOD_NDR                                                                                                                                                                                                                       |
| MTC_MOD_INCOME_NDR       | Number of units for moderate income non-deed restricted         | Number     | IF CO_MOD_INCOME_NDR_CON_ENT_PERM > 0, THEN CO_MOD_INCOME_NDR_CON_ENT_PERM ELSE IF BP_MOD_INCOME_NDR_CON_ENT_PERM THEN BP_MOD_INCOME_NDR_CON_ENT_PERMELSE IF MOD_INCOME_NDR_CON_ENT_PERMITS > 0 THEN MOD_INCOME_NDR_CON_ENT_PERMITS             |
| MTC_MOD_INCOME_DR        | Number of units for moderate income deed restricted             | Number     | IF CO_MOD_INCOME_DR_CON_ENT_PERM > 0, THEN CO_MOD_INCOME_DR_CON_ENT_PERM ELSE IF BP_MOD_INCOME_DR_CON_ENT_PERM THEN BP_MOD_INCOME_DR_CON_ENT_PERMELSE IF MOD_INCOME_DR_CON_ENT_PERMITS > 0 THEN MOD_INCOME_DR_CON_ENT_PERMITS                   |
| MTC_MAPPED               | Whether address has been geocoded correctly or not              | Checkbox   |                                                                                                                                                                                                                                                 |
| MTC_LOW_TOT              | Low income total units                                          | Number     | Sum of LOW_DR and LOW_NDR                                                                                                                                                                                                                       |
| MTC_LOW_INCOME_NDR       | Low income units non-deed restricted                            | Number     | IF CO_LOW_INCOME_NDR_CON_ENT_PERM > 0, THEN CO_LOW_INCOME_NDR_CON_ENT_PERM ELSE IF BP_LOW_INCOME_NDR_CON_ENT_PERM THEN BP_LOW_INCOME_NDR_CON_ENT_PERMELSE IF LOW_INCOME_NDR_CON_ENT_PERMITS > 0 THEN LOW_INCOME_NDR_CON_ENT_PERMITS             |
| MTC_LOW_INCOME_DR        | Low income units deed restricted                                | Number     | IF CO_LOW_INCOME_DR_CON_ENT_PERM > 0, THEN CO_LOW_INCOME_DR_CON_ENT_PERM ELSE IF BP_LOW_INCOME_DR_CON_ENT_PERM THEN BP_LOW_INCOME_DR_CON_ENT_PERMELSE IF LOW_INCOME_DR_CON_ENT_PERMITS > 0 THEN LOW_INCOME_DR_CON_ENT_PERMITS                   |
| MTC_LONG                 | Longitude in decimal degress                                    | Number     |                                                                                                                                                                                                                                                 |
| MTC_LAT                  | Latitude in decimal degress                                     | Number     |                                                                                                                                                                                                                                                 |
| MTC_ISSUE_DT             | Issue date                                                      | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_ID                   | Unique record identifier                                        | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_HOUSING_ELEMENT_SITE | Is address on a housing element site?                           | Checkbox   |                                                                                                                                                                                                                                                 |
| MTC_GEOCODE_TYPE         | Quality of geocoding (rooftop, range, geometric or approximate) | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_GEOCODE_ADDRESS      | Geocoded address                                                | Plain Text |                                                                                                                                                                                                                                                 |
| MTC_ABOVE_MOD_INCOME     | Above moderate income units                                     | Number     | IF CO_ABOVE_MOD_INCOME_CON_ENT_PERM > 0, THEN CO_ABOVE_MOD_INCOME_CON_ENT_PERM ELSE IF BP_ABOVE_MOD_INCOME_CON_ENT_PERM THEN BP_ABOVE_MOD_INCOME_CON_ENT_PERMELSE IF ABOVE_MOD_INCOME_CON_ENT_PERMITS > 0 THEN ABOVE_MOD_INCOME_CON_ENT_PERMITS |

## Geocoding

Geocoding is conducted using Google's geocoding engine. Records that return a geocoding type of ROOFTOP or RANGE_INTERPOLATED are considered accurate for the needs of the internal spatial analysis. Records returning geocoding types of GEOMETRIC_CENTER or APPROXIMATE are reviewed and manually geocoded where possible. 

All records are also checked to make sure that they fall within the bounds of the 9 county Bay Area region. 
| Latitude Bounds             | Longitude Bounds                                                           |
|--------------------------------|------------------------------------------------------------------------------|
| Min 36 Max 38 decimal degrees                   |    Min -123 Max -121 decimal degrees                                                                       |


## Spatial Analysis
Once geocoding is complete, all records are checked to see whether they fall inside Priority Development Areas, Transit Priority Areas and Housing Element Sites, and the appropriate fields (MTC_PDA, MTC_TPA, MTC_HOUSING_ELEMENT_SITE) are updated.

For 2018, these datasets were used:

[Priority Development Areas](https://opendata.mtc.ca.gov/datasets/priority-development-areas-plan-bay-area-2040)

[Transit Priority Areas](https://opendata.mtc.ca.gov/datasets/d97b4f72543a40b2b85d59ac085e01a0_0?geometry=-122.635%2C37.229%2C-121.482%2C37.420)

[Housing Element Sites](https://opendata.mtc.ca.gov/datasets/regional-housing-need-assessment-2015-2023-housing-element-sites?geometry=-122.410%2C37.801%2C-122.121%2C37.848)

