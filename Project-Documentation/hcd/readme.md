# Department of Housing and Community Development (HCD)

## Project Management

- [Box Directory (Internal Access Only)](https://mtcdrive.app.box.com/folder/108862836847?s=vmfbr9t4efl8rgavqvp1sx57dpx3sj86)
- [Asana Project](https://app.asana.com/0/1196225291559865/1196225291559890)

## Table of Contents 
- [Background](#background)
- [Data Sources](#data-sources)
	- [California Housing and Community Development Data](#california-housing-and-community-development-data)
	- [MTC Growth Areas Data](mtc-growth-areas-data)
- [Analysis Parameters]()
	- [Annual Progress Report Background](#annual-progress-report-background)
	- [Annual Progress Report Tables and Data Dictionaries](#annual-progress-report-tables-and-data-dictionaries)
- [Methodology]()
- [Results]()

## Background
From 2014-2017, MTC/ABAG underwent a process of collecting housing permit data from local jurisdictions based on their [Annual Progress Reports](https://www.hcd.ca.gov/community-development/housing-element/index.shtml). This was typically done via the use of a survey provided to jurisdictions, the results of which were then collated and analyzed to begin to provide a picture of housing production in the region. 

Based on these data, a housing portal website was developed to allow users to visualize these trends broken down by year, housing type and income category [Housing Data Portal](http://housing.abag.ca.gov)

Additionally, MTC used this housing permit data to inform it's [Housing Incentive Pool](https://mtc.ca.gov/our-work/fund-invest/investment-strategies-commitments/focused-growth/affordable-housing/housing) (HIP) grant program.

Starting in 2018, HCD provided a platform for jurisdictions county-wide to directly submit APR information to them via a web portal. Entitlement and certificate of occupancy data were collected along with housing permit data. 

MTC now collects this housing data annually directly from HCD.

## Data Sources

### California Housing and Community Development Data

[California Housing and Community Development (HCD) Website](https://www.hcd.ca.gov/community-development/housing-element/index.shtml)

The data are provided by HCD as a single excel workbook containing the data for the region, exported from their database. The data cannot currently be downloaded from their website publicly. 

[Housing Element Sites](https://opendata.mtc.ca.gov/datasets/regional-housing-need-assessment-2015-2023-housing-element-sites?geometry=-122.410%2C37.801%2C-122.121%2C37.848)

### MTC Growth Area Data

[Priority Development Areas](https://opendata.mtc.ca.gov/datasets/priority-development-areas-plan-bay-area-2040)

[Transit Priority Areas](https://opendata.mtc.ca.gov/datasets/d97b4f72543a40b2b85d59ac085e01a0_0?geometry=-122.635%2C37.229%2C-121.482%2C37.420)

## Analysis Parameters

### Annual Progress Report Background
Each jurisdiction (city council or board of supervisors) must prepare an annual progress report on the jurisdiction’s status and progress in implementing its housing element. (Government Code Section 65400.)

Each jurisdiction’s Annual Progress Report (APR) must be submitted to HCD and the Governor’s Office of Planning and Research (OPR) by April 1 of each year (covering the previous calendar year).

New APR form and instructions - for calendar year (CY) 2018 and 2019

AB 879 and SB 35 of the 2017 Housing Package, as well as AB 1486 (2019), added new data requirements for the Housing Element Annual Progress Reports (APRs). These changes are reflected in the new APR form and instructions, which are posted below.

- [APR form for CY 2018 and 2019](https://www.hcd.ca.gov/community-development/housing-element/docs/Housing-Element-Annual-Progress-Report-2019.xlsm) (XLS)
- [APR instructions for CY 2018 and 2019](https://www.hcd.ca.gov/community-development/housing-element/docs/Housing-Element-Annual-Progress-Report-Instructions-2019.pdf) (PDF)

### Annual Progress Report Tables and Data Dictionaries

1. Table A - Housing Development Applications 
2. Table A2 - New Construction, Entitled, Permits, and Completed Units
	- [Table A2 Data Dictionary](HCD_A2_Report_Data_Dictionary.csv)
3. Table B - Regional Housing Needs Allocation Progress – Permitted Units Issued By Affordability
4. Table C - Sites Identified or Rezoned to Accommodate Shortfall Housing Need
5. Table D - Program Implementation Status pursuant to Government Code section 65583 
6. Table E - Commercial Development Bonus Approved pursuant to Government Code

## Methodology

### Process Overview
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

## Results
[Housing APR Data (Internal Access Only)](https://data.bayareametro.gov/dataset/Housing-APR-Data-2018-2019/briv-ikjp)


