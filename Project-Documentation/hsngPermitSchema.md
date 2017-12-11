# Housing Schema - Residential Permit Attribute Table Structure

## Problem Statement
Develop structure for residential permit attribute table in housing schema of enterprise database. Purpose is to set rules and restrictions on permit attribute values to make it easier to write queries against the table.

## Outcome
The Housing Schema is in a PostgreSQL database. The attribute table structure, rules, and restrictions is found below. There is one table containing the attributes for each year. Queries and display for a particular year will be based on the permyear values. 

Full definitions for field name and domain values are found in the metadata associated with the data and services available on the internal data portal and the MTC, public ArcGIS Online and Open Data portals.

Field | Description | Rule, Restrictions, and Notes | Type | Length | Configuration | Default Value 
--- | --- | --- | :---: | :---: | --- | :---:
joinid | Connect feature to attribute | Organized by county. Each year increment by 10 over previous year's final value. | Text | 11 | char(11) NOT NULL | 
permyear | Permit year | Format is YYYY | Text | 4 | char(4) NOT NULL | 
permdate | Permit date | Format is MMM DD. <br/> Month values must be all caps. Date values 1-9 must have preceeding zero (0). | Text | 6 | varchar(6) | 
county | County FIP number | Format is 60XX. <br/> Values are limited to: <br/> 6001 - Alameda County <br/> 6013 - Contra Costa County <br/> 6041 - Marin County <br/> 6055 - Napa County <br/> 6075 - San Francisco <br/> 6081 - San Mateo County <br/> 6085 - Santa Clara County <br/> 6095 - Solano County <br/> 6097 - Sonoma County | Text | 4 | char(4) NOT NULL |
jurisdictn | Jurisdiction name | | Text | 25 | varchar(25) NOT NULL |
apn | Assessor's Parcel Number | | Text | 25 | varchar(25) |
address | Building street address | | Text | 100 | varchar(100) | 
zip | Zip Code | Format is XXXXX. <br/> Do not add 4-digit extension to Zip Code. | Text | 5 | varchar(5) | 
projname | Project Name | | Text | 254 | varchar(254) | 
hcategory | Permitted housing category(ies) | Only categories tracked by the California Department of Housing and Community Development (HCD) are permitted. Case and format must match those from allowed value list. <br/>Allowed values: <br/> 5+ - Five or more units <br/> 2-4 - two to four units <br/> SF - Single-family home <br/> MH - Mobile home <br/> SU - Secondary unit | Text | 10 | varchar(10) | 
verylow | Very low income unit | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
low | Low income unit | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
moderate | Moderate income unit | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
abovemod | Above moderate income unit | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
totalunit | Total number of units | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
infill | Infill units | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
affrdunit | Number of affordable units | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
deedaffrd | Number of deed restricted affordable units | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
asstaffrd | Number of affordable units achieved through public assistance | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
opnaffrd | Number of affordable units achieved without public assistance | Decimals and thousands separators not allowed in values. | Number | | integer NOT NULL | 0 
tenure | Ownership or rental | Allowed values: <br/> O - Ownership units <br/> R - Rental units | Text | 1 | varchar(1) | 
rpa | Rehabilitated, preserved, or acquired units | Allowed values: <br/> R - Rehabilitated <br/> P - Preserved <br/> A - Acquired | Text | 1 | varchar(1) | 
rhna | Units are on a Regional Housing Need Allocation housing opportunity site | Allowed values: <br/> Y - Yes, units are on a housing opportunity site <br/> N - No, units are not on a housing opportunity site | Text | 1 | char(1) NOT NULL | N 
rhnacyc | Regional Housing Need Allocation cycle the opportunity site was identified for | Allowed values: <br/> RHNA4 <br/> RHNA5 <br/> RHNA4&5 | Text | 7 | varchar(7) | 
pda | Units are in a Priority Development Area (PDA) | Allowed values: <br/> Y - Units are in a PDA <br/> N - Units are not in a PDA | Text | 1 | char(1) NOT NULL | N | 
pdaid | Priority Development Area join ID | | Text | 6 | varchar(6) | 
tpa | Units are in a Transit Priority Area (TPA) | Allowed values: <br/> Y - Units are in a TPA <br/> N - Units are not in a TPA | Text | 1 | char(1) NOT NULL | N 
hoa | Units are in a Housing Opportunity Area (HOA) | Allowed values: <br/> Y - Units are in a HOA <br/> N - Units are not in a HOA | Text | 1 | char(1) NOT NULL | N 
occertiss | Has an occupancy certificate been issued? | Allowed values: <br/> Y - A housing occupancy certificate has been issued <br/> N - A housing occupancy certificate has not been issued | Text | 1 | char(1) NOT NULL | N 
occertyr | Year occupancy certificate issued | Format is YYYY | Text | 4 | varchar(4) NOT NULL | 
occertdt | Date occupancy certificate issued | Format is MMM DD. <br/> Month values must be all caps. Date values 1-9 must have preceeding zero (0). | Text | 6 | varchar(6) | 
mapped | Was permit geolocated? | Allowed values: <br/> Y - Permit was geolocated <br/> N - Permit was not geolocated | Text | 1 | char(1) NOT NULL | N 
notes | Permit notes | | Text | 254 | text | 
 
## Results
The residential permit attribute table has been created in the enterprise database and had the attributes for all permits gathered to date uploaded to it.
