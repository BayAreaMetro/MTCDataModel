# Housing Database Table Schemas

## Problem Statement
Document structure of tables used in the housing database. The database was developed to update and maintain the residential building permit feature set and attribute table for the San Francisco Bay Region and provide data for a permit explorer web application.

## Outcome
The Microsoft SQL Server housing database receives new residential building permits through the [Project Mapper](http://project-mapper.us-west-2.elasticbeanstalk.com) web application. Once a new permit is added through the application, background processes determine whether the permit location intersects the following geographies; Priority Development Areas (PDA), Transit Priority Areas (TPA), and/or housing element sites (Housing Sites) identified to accomodate a jurisdiction's Regional Housing Need Allocation. After processing the permit point feature is added to the dbo.permitFeature table and its attributes are added to dbo.permit_new.

The housing database also serves data to the [Housing Permit Explorer](http://housing-test.us-west-2.elasticbeanstalk.com/map) web application. Users of the application can view residential building permits for the region by year, income level, and housing category. The housing database also provides the PDA, TPA, and Housing Sites feature sets, used to process the intersect analysis for new permits, to the permit explorer as optional viewing layers.

The housing database has been designed, for the most part, to place few restrictions on how the data is formatted and does not enforce value contraints. Formatting, default values, and constraint rules are taken care of by the Project Mapper application code and are coded in enterprise database used by Metropolitan Transportation Commission staff.

## Database Table Schemas

[dbo.county](#dbo.county)<br/>
[dbo.jurisction](#dbo.jurisdiction)


#### dbo.county
Header 1 | Header 2
-------- | --------
Content  | Content

Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
name | nvarchar(50) | Yes | 
countyId | int | Yes | 
shape | geometry | Yes | 
wkt | nvarchar(MAX) | Yes | 


#### dbo.jurisdiction
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
jurisdictionId | int | Yes | 
name | nvarchar(50) | Yes | 
county_fips | int | Yes | 
county | nvarchar(17) | Yes | 
wkt | nvarchar(MAX) | Yes |
shape | geometry | Yes | 


#### dbo.jurisdictionPolicy
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
jurisdictionId | int | Yes | 
policyID | int | Yes | 
categoryID | int | Yes | 


#### dbo.permit
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
joinid | nvarchar(255) | No | Value to join attributes to mapped permits. 
permyear | nvarchar(255) | Yes | Year building permit was issued. 
permdate | nvarchar(255) | Yes | Date, as month and day (MMMDD), building permit was issued. 
county | nvarchar(255) | Yes | Name of county where permit was issued. 
jurisdictn | nvarchar(255) | Yes | City/town name or county name, for unincorporated areas, who issued the permit; where the new housing is located. 
apn | nvarchar(255) | Yes | Assessor Parcel Number 
address | nvarchar(255) | Yes | Street address where permitted housing is located. 
zip | nvarchar(255) | Yes | Zip Code for the street address. 
projname | nvarchar(255) | Yes | Name of the residential development project. 
hcategory | nvarchar(255) | Yes | Housing category(ies) contained in the permit. 
verylow | float | Yes | Number of permitted units affordable to very low income households (making between 0% and 50% of Area Median Income). Units serving extremely low income households are included in this category. 
low | float | Yes | Number of permitted units affordable to low income households (making between 50% and 80% of Area Median Income). 
moderate | float | Yes | Number of permitted units affordable to moderate income households (making between 80% and 120% of Area Median Income). 
abovemod | float | Yes | Number of permitted units affordable to above moderate income households (making more than 120% of Area Median Income). 
totalunit | float | Yes | Number of permitted units for all affordability levels. Whenever possible, this field records the total units per location for mapping purposes. <br/>**Note:** Some jurisdictions did not provide all of their affordability information by permit. In these cases, affordability information was captured, often as a sum for multiple permits, in a separate row with "Unidentified" listed under address and apn and are not mapped. These rows have "0" in the total unit field to ensure that there is no double counting of units. 
infill | float | Yes | Identifies whether units permitted units are located in an existing urbanized area (infill development).
affrdunit | float | Yes | Number of affordable units within the residential building permit.
deedaffrd | float | Yes | Number of affordable units within the residential building permit that have deed restrictions for long-term affordability recorded to the title.
asstaffrd | float | Yes | Number of affordable units within the residential building permit that obtain their affordability through a public subsidy or other public program.
opnaffrd | float | Yes | Number of affordable units within the residential building permit that obtain their affordability through market-based means.
tenure | nvarchar(255) | Yes | Identifies whether permitted units are proposed or planned for initial occupancy for renter occupants, owner occupants, or both where apparent at time of permit application. 
rpa | nvarchar(255) | Yes | Designates units permitted as rehabilitation/preservation/acquisition units.
rhna | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located on a site identified in a jurisdiction's Housing Element site inventory. 
rhnacyc | nvarchar(255) | Yes | Identifies the Regional Housing Need Allocation (RHNA) version used to determine whether unit(s) within the residential permits are within a Housing Element site. The location of residential permits are compared to the parcels that comprise the Housing Element site inventory in effect when the permit was issued. The parcels in the Housing Element site inventory change with each new RHNA cycle as jurisdictions are required to plan for their new allocation. 
pda | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located in a Priority Development Area (PDA). 
pdaid | nvarchar(255) | Yes | When units are located in a Priority Devlopment Area (PDA), this field provides the PDA identification key required to query residential building permits by PDA. 
pdajoinkey | nvarchar(50) | Yes | Same as the pdaid field. 
tpa | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located in a Transit Priority Area (TPA). 
hoa | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located in a High Opportunity Area (HOA). 
housingElementSites | nchar(10) | Yes | Same as the rhna field. 
occertiss | nvarchar(255) | Yes | Identifies whether permitted units have received an occupancy certificate.
occertyr | nvarchar(255) | Yes | Year the occupancy certificate was issued.
occertdt | nvarchar(255) | Yes | Date, as month and day (MMMDD), occupancy certificate was issued.
mapped | nvarchar(255) | Yes | Identifies whether the residential building permit was geolocated. Geolocation relied on information available at the time the permit was processed by the Metropolitan Transportation Commission (MTC). 
notes | nvarchar(MAX) | Yes | Note/comment made by either jurisdiction or Metropolitan Transportation Commission (MTC) staff regarding the residential building permit. 
jurisdictionId | int | Yes | Value to query residential building permits by jurisction for the Housing Permit Explorer. 


#### dbo.permit_new
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
joinid | nvarchar(255) | No | Value to join attributes to mapped permits. 
permyear | float | Yes |  Year building permit was issued. 
county | nvarchar(255) | Yes | Name of county where permit was issued. 
jurisdictn | nvarchar(255) | Yes | City/town name or county name, for unincorporated areas, who issued the permit; where the new housing is located. 
apn | nvarchar(255) | Yes | Assessor Parcel Number 
address | nvarchar(500) | Yes | Street address where permitted housing is located. 
zip | nvarchar(255) | Yes | Zip Code for the street address. 
projname | nvarchar(255) | Yes | Name of the residential development project. 
hcategory | nvarchar(255) | Yes |  Housing category(ies) contained in the permit. 
vlowtot | int | Yes | Total number of permitted units affordable to very low income households (making between 0% and 50% of Area Median Income). Units serving extremely low income households are included in this category. 
vlowdr | float | Yes | Number of permitted units affordable to very low income households that have deed restrictions for long-term affordability recorded to the title. 
vlowndr | float | Yes | Number of permitted units affordable to very low income households that are not deed restricted. 
lowtot | float | Yes | Total number of permitted units affordable to low income households (making between 50% and 80% of Area Median Income). 
lowdr | float | Yes | Number of permitted units affordable to low income households that have deed restrictions for long-term affordability recorded to the title. 
lowndr | float | Yes | Number of permitted units affordable to low income households that are not deed restricted. 
modtot | float | Yes | Total number of permitted units affordable to moderate income households (making between 80% and 120% of Area Median Income). 
moddr | float | Yes | Number of permitted units affordable to moderate income households that have deed restrictions for long-term affordability recorded to the title. 
modndr | float | Yes | Number of permitted units affordable to moderate income households that are not deed restricted. 
amodtot | float | Yes | Total number of permitted units affordable to above moderate income households (making more than 120% of Area Median Income). 
totalunit | float | Yes | Total number of permitted units for all affordability levels. Whenever possible, this field records the total units per location for mapping purposes. <br/>**Note:** Some jurisdictions did not provide all of their affordability information by permit. In these cases, affordability information was captured, often as a sum for multiple permits, in a separate row with "Unidentified" listed under address and apn and are not mapped. These rows have "0" in the total unit field to ensure that there is no double counting of units. 
tenure | nvarchar(255) | Yes | Identifies whether permitted units are proposed or planned for initial occupancy for renter occupants, owner occupants, or both where apparent at time of permit application. 
mapped | nvarchar(2) | Yes | Identifies whether the residential building permit was geolocated. Geolocation relied on information available at the time the permit was processed by the Metropolitan Transportation Commission (MTC). 
mapnotes | nvarchar(500) | Yes | For non-geolocated permits, this field identifies the reason the permit was unable to be mapped. 
pda | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located in a Priority Development Area (PDA). 
pdacycle | nvarchar(255) | Yes | Identifies the Priority Development Area (PDA) version used to determine whether unit(s) within the residential permits are within a PDA boundary. PDA boundaries can change over time. The result is that permits identified as being within a PDA may not be in one when compared against a PDA version other than the one they were originally compared to. 
pdajoinid | nvarchar(255) | Yes | When units are located in a Priority Devlopment Area (PDA), this field provides the PDA identification key required to query residential building permits by PDA. 
tpa | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located in a Transit Priority Area (TPA). 
tpacycle | nvarchar(100) | Yes | Identifies the Transit Priority Area (TPA) version used to determine whether unit(s) within the residential permits are within a TPA boundary. TPA boundaries can change over time. The result is that permits identified as being within a TPA may not be in one when compared against a TPA version other than the one they were originally compared to. 
hsngsite | nvarchar(255) | Yes | Identifies whether the unit(s) within the residential project are located on a site identified in a jurisdiction's Housing Element site inventory. 
rhnacycle | nvarchar(255) | Yes | Identifies the Regional Housing Need Allocation (RHNA) version used to determine whether unit(s) within the residential permits are within a Housing Element site. The location of residential permits are compared to the parcels that comprise the Housing Element site inventory in effect when the permit was issued. The parcels in the Housing Element site inventory change with each new RHNA cycle as jurisdictions are required to plan for their new allocation. 
notes | nvarchar(MAX) | Yes | Note/comment made by either jurisdiction or Metropolitan Transportation Commission (MTC) staff regarding the residential building permit. 
jurisdictionId | int | Yes | Value to query residential building permits by jurisction for the Housing Permit Explorer. 


#### dbo.permitDataDictionary
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
attribute | nvarchar(50) | Yes | 
description | nvarchar(500) | Yes | 


#### dbo.permitDataDomainValues
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
attribute | nvarchar(50) | Yes | 
domain | nvarchar(50) | Yes | 
description | nvarchar(500) | Yes | 


#### dbo.permitFeature
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
OBJECTID | int | No | 
joinid | nvarchar(20) | Yes | 
Lat | numeric(38,8) | Yes | 
Long | numeric(38,8) | Yes | 
WKT | nvarchar(MAX) | Yes | 
Shape | geometry | Yes | 


#### dbo.policy
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
id | int | No | 
policy | nvarchar(100) | Yes | 
description | nvarchar(200) | Yes | 
policyId | int | Yes | 
categoryId | int | Yes | 
toolkit | nvarchar(MAX) | Yes | 
toolkit_summary_and_benefits | nvarchar(MAX) | Yes | 
toolkit_who_implements | nvarchar(MAX) | Yes | 
toolkit_model_ordinances | nvarchar(MAX) | Yes | 
display | nchar(10) | Yes | 
tags | nvarchar(500) | Yes | 


#### dbo.policyCategory
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
_id | int | No | 
categoryId | int | Yes | 
category | nvarchar(50) | Yes | 


#### dbo.rhna_2015-2035
Column Name | Column Type | Allow Nulls | Definition 
--- | --- | :---: | --- 
Jurisdiction Name | nvarchar(255) | Yes | 
very_low_rhna | int | Yes | 
very_low_non_dr | int | Yes | 
very_low_dr | int | Yes | 
low_rhna | int | Yes | 
low_non_dr | int | Yes | 
low_dr | int | Yes | 
moderate_rhna | int | Yes | 
moderate_non_dr | int | Yes | 
moderate_dr | int | Yes | 
above_moderate_rhna | int | Yes | 
above_moderate_total | int | Yes | 
