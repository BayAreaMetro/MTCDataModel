# Housing Schema - Residential Permit Attribute Table Structure

## Problem Statement
Develop structure for residential permit attribute table in housing schema of enterprise database. Purpose is to set rules and restrictions on permit attribute values to make it easier to write queries against the table.

## Outcome
The Housing Schema is in a PostgreSQL database. The attribute table structure, rules, and restrictions are found below. There is one table containing the attributes for the permits gathered each year. Queries and display for a particular year are based on the permyear values. 

Full definitions for field name and domain values are found in the metadata associated with the services available on the MTC  ArcGIS Online and Open Data portals.

Column Name | Column Type | Not Null | Default Value | Constraint | Note 
--- | --- | :---: | :---: | --- | --- 
objectid | integer | X | nextval | | | 
joinid | character(11) | X | | UNIQUE | Format is CCCC#######. When new permits are gathered, increment joinid by at least 10 over previous year's final value for each county. |
permyear | character(4) | X | | | Format is YYYY. | 
county | character(4) | X | | Allowed Values: <ul><li>6001 <li>6013 <li>6041 <li>6055 <li>6075 <li>6081 <li>6085 <li>6095 <li>6097</ul> | Format is 60##. | 
jurisdictn | character varying(27) | X | | | | 
apn | character varying(25) | | | | | 
address | character varying(100) | | | | | 
zip | character varying(5) | | | | Format is #####. Do not add 4-digit Zip Code extension. | 
projname | character varying(254) | | | | | 
hcategory | character varying(12) | | | | Only categories tracked by the CA Dept of Housing and Community Development (HCD) are permitted. Allowed values are 5+ (five or more units, multifamily), 2-4 (two to four units), SF (single-family home), MH (mobile home), and SU (secondary unit). There can be more than one housing category value entered. If a non-permitted housing category value is submitted, convert to equivalent allowed value and place original value in notes. | 
vlowdr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
vlowndr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
vlowtot | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
lowdr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
lowndr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
lowtot | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
moddr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
modndr | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
modtot | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
amodtot | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
totalunit | integer | X | 0 | | Must be whole numbers. Thousands separators and decimals are not allowed. | 
tenure | character varying(1) | | | Allowed Values: <ul><li>O <li>R <li>A <li><<i>null</i>></ul> | | 
mapped | character(1) | X | N | Allowed Values: <ul><li>Y <li>N</ul> | | 
mapnotes | character varying(45) | | | Allowed Values: <ul><li>Affordability Not Assigned by Permit Location <li>No Development <li>No Response <li><<i>null</i>></ul> | | 
pda | character(1) | X | N | Allowed Values: <ul><li>Y <li>N</ul> | | 
pdacycle | character varying(4) | | | | |
pdajoinid | character varying(6) | | | | |
tpa | character(1) | X | N | Allowed Values: <ul><li>Y <li>N</ul> | | 
tpacycle | character varying(4) | X | | | |
hsngsite | character(1) | X | N | Allowed Values: <ul><li>Y <li>N</ul> | | 
rhnacycle | character(9) | | | Allowed Values: <ul><li>2007-2014 <li>2015-2023 <li><<i>null</i>></ul> | | 
notes | text | | | | | 
