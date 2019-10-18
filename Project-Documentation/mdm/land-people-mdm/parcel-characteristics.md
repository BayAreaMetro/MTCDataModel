-Draft-

# Parcel Regional Characteristics

### Description, Purpose, and Use
This documentation provides a high-level overview of the Parcel Regional Characteristics dataset. This dataset includes characteristics of the region's parcels including -- but not limited to -- land use, building characteristics, and monetary value. These characteristics are used in MTC/ABAG land use modeling, housing policy, and long range planning research. This dataset is the source of the UrbanSim Building and Parcels Datasets that are used for Plan Bay Area 2050's UrbanSim models.

### Project Management

- [Data processing folder](https://mtcdrive.app.box.com/folder/90613500867)

### Contents 

- [Data Collection](#data-collection)
- [Field Mapping and Documentation](#field-mapping-and-documentation)
- [Methodology](#methodology)
- [Outputs](#outputs)
- [Related Works](#related-works)


## Data Collection  
This dataset was compiled using parcel characteristics data from each of the nine counties' assessor's offices.


## Field Mapping and Documentation

**NOTE**: Field documentation available internally at MTC only.

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

### Field Mapping

**Parcel Regional Characteristics**|**Description**|**Alameda**|**Contra Costa**|**Marin**|**Napa**|**San Francisco**|**San Mateo**|**Santa Clara**|**Solano**|**Sonoma**|**Source**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
parcel\_id|Unique join id which joins buildings to parcels| | | | | | | | | |MTC derived
jurisdiction|City or county (unincorporated area) name|city\_fixed|situs\_city\_abbr|situs\_city|(Calculated Value) case when case when situs2 in ('', 'nan', 'NULL', null) then null else situs2 end is not null then case when situs2 in ('', 'nan', 'NULL', null) then null else situs2 end when case when community in ('', 'nan', 'NULL', null)  then null else community end is not null then case when community in ('', 'nan', 'NULL', null)  then null else community end else null end| |situs\_city|city\_code|site\_city|situscity|County Assessor derived (with MTC mapping)
fipco|County FIPS code|fipco|fipco|fipco|fipco|fipco|fipco|fipco|fipco|fipco|MTC derived
apn|County APN|Assessor's Parcel Number (APN) sort format, Sort Parcel|PARCEL NUMBER|property\_id|Asmt|KEY, OWNR-KEY, RP1PRCLID|APN|APN|PARCEL NUMBER, ASSESSOR PARCEL NUMBER|ParcelNumber|County Assessor derived (with MTC mapping)
building\_id|Unique building ID|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|(Calculated Value) building\_id|MTC/County Assessor derived
building\_type|The UrbanSim building type or the primary building type if there are multiple| | | | | | | | | |MTC derived
building\_sqft|Square footage of building(s)|building\_area|(Calculated Value) coalesce(building\_1\_sq\_feet, 0) + coalesce(residence\_2nd\_floor\_sq\_ft, 0) + coalesce(residence\_lower\_level\_sq\_ft, 0)|liv\_area\_sqft|buildingsize|sqft|(Calculated Value) case when source\_file = 'resident' then coalesce(third\_floor\_area, 0) + coalesce(second\_floor\_area, 0) + coalesce(garage\_area, 0) + coalesce(first\_floor\_area, 0) + coalesce(finished\_basement\_area, 0) + coalesce(basement\_area, 0) + coalesce(base\_area, 0) + coalesce(attic\_area, 0) + coalesce(area\_of\_addition, 0) when source\_file =  'mobilehome' then total\_sq\_ft when source\_file =  'condo' then coalesce(base\_area, 0) + coalesce(garage\_area, 0) when source\_file in ('multifam', 'industrial',  'hotel') then gross\_building\_area\_fixed else null end|total\_area|total\_area\_of\_building|(Calculated Value) coalesce(buildingprimarysize, 0) +  coalesce(buildingsecondarysize, 0)|MTC/County Assessor derived
non\_residential\_sqft|Square footage of non-residential space in building(s)|building\_area|building\_1\_sq\_feet| |buildingsize|sqft|gross\_building\_area\_fixed|total\_area|total\_area\_of\_building|(Calculated Value) coalesce(buildingprimarysize, 0) +  coalesce(buildingsecondarysize, 0)|MTC/County Assessor derived
residential\_units|Number of residential units in building(s)| number\_of\_units|(Calculated Value) case when pdr\_type = 'O' then total\_rooms else case when use\_code in (11, 12, 14) then 1 when use\_code in (13, 16, 21) then 2 when use\_code = 22 then 3 when use\_code = 23 then 4 when use\_code = 25 then 8.5 when use\_code = 26 then 18.5 when use\_code = 27 then 42 when use\_code = 28 then 60 else null end end| living\_units|(Calculated Value) case when usecode in ('05', '05E', '11') then 1 when usecode in ('212', '2122') then 2 when usecode in ('213', '2133') then 3 when usecode in ('214', '2144') then 4 when usecode = '215' then 7 when usecode = '216' then 14.5 when usecode = '217' then 34.5 when usecode = 218 then 50 else null end| units| (Calculated Value) case when property\_use\_code in (2, 92) then 2 when property\_use\_code in (3, 93) then 3 when property\_use\_code in (4, 94) then 4 when property\_use\_code in (5, 96) then 5 when source\_file in ('resident', 'mobilehome') or property\_use\_code = 1 then 1 when source\_file = 'multifam' and units\_allowed is not null then units\_allowed when source\_file = 'condo' and no\_of\_units is not null then no\_of\_units else null end|(Calculated Value) case when number\_units is not null then number\_units else case use\_code\_fixed when 1 then 1 when 2 then 2 when 3 then 3.5 when 4 then 5 else null end end|  (Calculated Value) case when source\_file = 'Official Roll' then case when left(use\_code, 2) in (10, 12, 15) then 1 when use\_code = 2100 then number\_of\_units else null end else null end|(Calculated Value) coalesce(buildingprimaryunitcount, 0) + coalesce(buildingsecondaryunitcount, 0)|MTC/County Assessor derived
year\_built|Year building was built or average if multiple|year\_built|year\_built|construct\_yr|yearbuilt|yrblt|year\_built\_fixed|year\_built|year\_built|buildingprimaryyearbuilt|MTC/County Assessor derived
asssessed\_land\_value|Assessor's value of parcel land| land|land\_value|land\_value| currentmarketlandvalue| rp1lndval|land\_value|landvalue|land\_value| value601land|County assessor derived
assessed\_building\_value|Assessor's value of the building(s)|imps|improvement\_value|imp\_value|currentstructuralimprvalue| rp1impval|improvement\_value|securedimprove|improvement\_value| value601netvalue|County assessor derived
land\_improvement\_ratio|Assessed land value / Assessed building value| land\_improvement\_ratio|(Calculated Value) land\_value/(improvement\_value + .0000001)|(Calculated Value) land\_value/(imp\_value + .0000001)| (Calculated Value) currentmarketlandvalue/(currentnetvalue + .0000001)| (Calculated Value) rp1lndval/(rp1impval + .0000001)|(Calculated Value) land\_value/(improvement\_value+ .0000001)|(Calculated Value) landvalue/(securedimprove + .0000001)|(Calculated Value) land\_value/(improvement\_value + .0000001)| (Calculated Value) value601land/(value601structure + .0000001)|MTC/County Assessor derived
assessed\_date|Date on which assesment occurred|doc\_dt| |recordation\_dt|dts| valdate|date\_of\_record| date\_updated| |asmtstatusdate|County assessor derived
last\_sale\_price|Price in dollars for the last building transaction| value\_from\_trans\_tax| | | | recurrpric| last\_sale\_amount| | | salesalesprice|County assessor derived
last\_sale\_date|Date of the last building transaction| transfer\_dt| | |transdate1| recurrsald| date\_of\_last\_sale| datetransfer| | salerecordingdate|County assessor derived
use\_code|Land use ID|use\_code\_fixed| use\_code| use\_cd|usecode| rp1clacde|property\_use\_code|use\_code\_fixed| use\_code|usecode|County assessor derived
use\_code\_desc|Land use description| | | | | | | | | |MTC/County Assessor derived
address|Parcel address|(Calculated Value) case when street\_num\_fixed in (null, '', 'nan') then '' else street\_num\_fixed || ' ' end || case when pre\_dir in (null, '', 'nan') then '' else pre\_dir || ' ' end || case when street\_name\_fixed in (null, '', 'nan') then '' else street\_name\_fixed || ' ' end || case when street\_suffix  in (null, '', 'nan') then '' else street\_suffix || ' ' end || case when post\_dir in (null, '', 'nan') then '' else post\_dir || ' ' end || case when unit\_desig in (null, '', 'nan') then '' else unit\_desig || ' ' end || case when unit\_num\_fixed  in (null, '', 'nan') then '' else unit\_num\_fixed || ' ' end || case when city\_fixed in (null, '', 'nan') then '' else city\_fixed || ' ' end || case when zip\_code\_fixed in (null, '', 'nan') then '' else zip\_code\_fixed || ' ' end|(Calculated Value) case when situs\_street\_nbr in (null, 'nan', '') then '' else situs\_street\_nbr || ' ' end || situs\_street\_name || ' ' || case when situs\_street\_suffix in (null, 'nan', '') then '' else situs\_street\_suffix || ', ' end || situs\_city\_abbr || ', CA ' || situs\_zip|(Calculated Value) case when situs\_formatted in (null, 'nan', '') then '' else situs\_formatted || ' ' end || case when situs\_city in (null, 'nan', '') then '' else situs\_city || ', CA' end|(Calculated Value) case when case when situs1 in ('', 'nan', 'NULL', null) then '' else situs1 || ', ' end || case when situs2 in ('', 'nan', 'NULL', null) then '' else situs2 end <> ''    then case when situs1 in ('', 'nan', 'NULL', null) then '' else situs1 || ', ' end || case when situs2 in ('', 'nan', 'NULL', null) then '' else situs2 end when case when situs1 in ('', 'nan', 'NULL', null) then '' else situs1 || ', ' end || case when situs2 in ('', 'nan', 'NULL', null) then '' else situs2 end = ''and case when streetaddr in ('', 'nan', 'NULL', null) then '' else streetaddr || ', ' end || case when community in ('', 'nan', 'NULL', null) then '' else community end <> ''    then case when streetaddr in ('', 'nan', 'NULL', null) then '' else streetaddr || ', ' end || case when community in ('', 'nan', 'NULL', null) then '' else community end else null end|address|(Calculated Value) case when situs\_no1 in (null, 'nan', '') then '' else situs\_no1 || ' ' end || case when situs\_direction in (null, 'nan', '') then '' else situs\_direction || ' ' end || case when situs\_street in (null, 'nan', '') then '' else situs\_street || ' ' end || case when situs\_street\_type in (null, 'nan', '') then '' else situs\_street\_type || ', ' end || case when situs\_street\_box in (null, 'nan', '') then '' else situs\_street\_box || ', ' end || case when situs\_city in (null, 'nan', '') then '' else situs\_city || ', CA' end|(Calculated Value) case when house\_number in (null, 'nan', '') then '' else house\_number || '' end || case when house\_suffix in (null, 'nan', '') then '' else house\_suffix || ', ' end || case when unit\_number in (null, 'nan', '') then '' else 'Unit ' || unit\_number || ', ' end || case when street\_direction in (null, 'nan', '') then '' else street\_direction || ' ' end || case when street\_name in (null, 'nan', '') then '' else ' ' || street\_name || ' ' end || case when street\_suffix in (null, 'nan', '') then '' else street\_suffix || ', ' end || case when city\_code in (null, 'nan', '') then '' else city\_code || ', CA' end|(Calculated Value) case when situs\_street\_number in (null, 'nan', '') then '' else situs\_street\_number || ' ' end || case when situs\_street\_name in (null, 'nan', '') then '' else situs\_street\_name || ', ' end || case when site\_building in (null, 'nan', '') then '' else 'Building ' || site\_building || ', ' end || case when site\_unit\_ in (null, 'nan', '') then '' else 'Unit ' || site\_unit\_ || ', ' end || case when site\_city in (null, 'nan', '') then '' else site\_city || ', CA' end|(Calculated Value) case when situsformatted1 in (null, 'nan', '', 'NONE') then '' else situsformatted1 || ', ' end || situsformatted2|MTC/County Assessor derived
building\_stories|Number of stories in building(s)|number\_of\_stories|(Calculated Value) case when residence\_lower\_level\_sq\_ft > 0 then 1 when residence\_2nd\_floor\_sq\_ft > 0 then 2 else null end| | |(Calculated Value) case when storeyno ~ '^([0-9]+[.]?[0-9]*|[.][0-9]+)$' then cast(storeyno as float) else null end|(Calculated Value) case when  \_\_of\_story is not null then \_\_of\_story else case when first\_floor\_area > 0 then 1 when second\_floor\_area > 0 then 2 when third\_floor\_area > 0 then 3 else null end end|(Calculated Value) case when first\_floor\_area > 0 then 1 when second\_flr\_area > 0 then 2 when third\_floor\_area > 0 then 3 when number\_floors > 0 then number\_floors else null end|(Calculated Value) case when area\_of\_first\_floor > 0 then 1 when area\_of\_second\_floor > 0 then 2 when area\_of\_third\_floor > 0 then 3 else null end|buildingprimarystories|MTC/County Assessor derived
bedrooms|Number of bedrooms in residence| number\_of\_bedrooms| bedrooms| nbr\_bedrooms| bedrooms| beds| number\_of\_bedrooms\_fixed| bedroom| number\_of\_bedrooms| buildingprimarybedrooms|County assessor derived
bathrooms|Number of bathrooms| number\_of\_bathrooms| bathrooms| nbr\_bathrooms| bathrooms| baths| number\_of\_bathrooms\_fixed| (Calculated Value) case when bath\_rooms ~ '^([0-9]+[.]?[0-9]*|[.][0-9]+)$' then cast(bath\_rooms as float) else null end| number\_of\_baths| buildingprimarybaths|County assessor derived
rentable\_sqft|Rentable square-footage|rentable\_space| | | | |net\_rent\_area|rentable\_area| | | 
lot\_sqft|Lot square-footage|lot\_size|area|land\_sqft|landsqft|larea| land\_sq\_\_feet| (Calculated Value) land\_acres/43560| lot\_size\_\_sq\_\_ft\_\_| landsizesqft|County assessor derived


## Methodology

**Figure 1.** Data Processing Overview

![Data Processing Diagram](https://www.lucidchart.com/publicSegments/view/cedfcb98-baf0-4946-849d-9a2861625378/image.png)

[**Detailed data processing methodology**](https://mtcdrive.app.box.com/file/542714111844)(**NOTE**: Available internally at MTC only.)


## Outputs

**NOTE**: Output tables available internally at MTC only.

[Parcel Regional Characteristics](https://data.bayareametro.gov/Cadastral/Parcel-Regional-Characteristics/8wj7-fdzw)

**Derived Datasets:**

- [Urbansim Buildings](https://data.bayareametro.gov/Land-Use/UrbanSim-Buildings/huqe-evqw)
- [Urbansim Parcels](https://data.bayareametro.gov/Land-Use/UrbanSim-Parcels/6axv-s6xn)


## Related Works 

#### County Assessor Data

**NOTE**: County Assessor datasets available internally at MTC only.

- [Alameda](https://data.bayareametro.gov/Cadastral/Alameda_Assessor_Data/itip-ty3s)
- [Contra Costa](https://data.bayareametro.gov/Cadastral/Contra_Costa_Assessor_Data/tbaa-fxhj)
- [Marin](https://data.bayareametro.gov/Cadastral/Marin_Assessor_Data/a5g6-4rp7)
- [Napa](https://data.bayareametro.gov/Cadastral/Napa_Assessor_Data/j3be-m2q7)
- [San Francisco](https://data.bayareametro.gov/Cadastral/San_Francisco_Assessor_Data/h9qg-ba8m)
- [San Mateo](https://data.bayareametro.gov/Cadastral/San_Mateo_Assessor_Data/y9fw-qqxx)
- [Santa Clara](https://data.bayareametro.gov/Cadastral/Santa_Clara_Assessor_Data/qzkh-5ea9)
- [Solano](https://data.bayareametro.gov/Cadastral/Solano_Assessor_Data/ap9i-mfk9)
- [Sonoma](https://data.bayareametro.gov/Cadastral/Sonoma_Assessor_Data/fb89-2kiu)


### Related Datasets

- [Parcels 2018](https://data.bayareametro.gov/Cadastral/Parcels-2018/fqea-xb6g) | Join Field: Parcels 2018.joinid = parcel_id

