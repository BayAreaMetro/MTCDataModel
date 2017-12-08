# Housing Schema - Residential Permit Attribute Table

## Problem Statement
Develop structure for residential permit attribute table in housing schema of enterprise database. Purpose is to set rules and restrictions on permit attribute values to make it easier to write queries against the table.

## Outcome
The Housing Schema is in a PostgreSQL database. The attribute table structure, rules, and restrictions is found below. Full definitions for field name and domain values are found in the metadata associated with the data and services available on the internal data portal.

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

## Results
