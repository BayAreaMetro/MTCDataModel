-Draft-

# Regional Parcel Characteristics

### Description, Purpose, and Use
This documentation provides a high-level overview of the Regional Parcel Database's wide variety of fields. These fields describe characteristics of the region's parcels including -- but not limited to -- land use, building characteristics, and monetary value. These characteristics are used in MTC/ABAG land use modeling, housing policy, and long range planning research. The database has significant overlap with the UrbanSim Building and Parcels Datasets that are used for Plan Bay Area 2050's UrbanSim models.

### Project Management

- [Asana Project]
- [Box](https://mtcdrive.app.box.com/folder/79744886422)  

### Contents 

- [Field Mapping, Definitions, and Sources](#field-mapping,-definitions,-and-sources)
- [Data Collection](#data-collection)
- [Fields](#methodology)
    - [Alameda County](#alameda-county)
    - [Contra Costa County](#contra-costa-county)
    - [Marin County](#marin-county)
    - [Napa County](#napa-county)
    - [San Francisco (City and County)](#san-francisco-city-and-county)
    - [San Mateo County](#san-mateo-county)
    - [Santa Clara County](#santa-clara-county)
    - [Solano County](#solano-county)
    - [Sonoma County](#sonoma-county)
- [Related Works](#related-works)

## Field Mapping, Definitions, and Sources

**NOTE**: Field documentation available internally at MTC only.

* **Alameda County**
   * [Alameda County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Alameda_Buildings_Field_Mapping.csv)
   * [Alameda County Assessor Field Documentation](https://mtcdrive.box.com/s/9nje22hvxgeri0pwb05dd4j0xrhr84mv)
* **Contra Costa County**
   * Contra Costa County Field Mapping (**Not Currently Available**)
   * [Contra Costa County Assessor Field Documentation](https://mtcdrive.box.com/s/65px7q9wzl8ge0pwgjatt0bqyjdtbqjx)
* **Marin County**
   * [Marin County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Marin_Buildings_Field_Mapping.csv)
   * [Marin County Assessor Field Documentation](https://mtcdrive.box.com/s/nahof8uz18qzqrl1i7zmzv7by0zqjslm)
* **Napa County**
   * [Napa County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Napa_Buildings_Field_Mapping.csv)
   * Napa County Assessor Field Documentaiton (**Not Currently Available**)
* **San Francisco County**
   * [San Francisco County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SF_Buildings_Field_Mapping.csv)
   * [San Francisco County Assessor Field Documentation](https://mtcdrive.box.com/s/8xyhr6uicc68be0boyqtv7fvcmun3mue)
* **San Mateo County**
   * [San Mateo County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SM_Buildings_Field_Mapping.csv)
   * [San Mateo County Assessor Field Documentation](https://mtcdrive.box.com/s/bai2l1erwum07rwk28dcsy05j4bcnpbo)
* **Santa Clara County**
   * [Santa Clara County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/SC_Buildings_Field_Mapping.csv)
   * [Santa Clara County Assessor Field Documentation](https://mtcdrive.box.com/s/jd12binabjjnz7bigg50ajubgvgmj6do)
* **Solano County**
   * [Solano County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Solano_Buildings_Field_Mapping.csv)
   * [Solano County Assessor Field Documentation](https://mtcdrive.box.com/s/idafksdkt4yv3ekojfnez8j463hlrpmo)
* **Sonoma County**
   * [Sonoma County Field Mapping](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/land-people-mdm/files/Sonoma_Buildings_Field_Mapping.csv)
   * [Sonoma County Assessor Field Documentation](https://mtcdrive.box.com/s/oi7065zrci2gu376f45yxa65n0fnwy9o)

## Data Collection  
This dataset was compiled using parcel characteristics data from each of the nine counties' assessor's offices. The figure below is an entity relationship diagram (ERD) in third normal form explaining the interactions within the database.

## Fields

Parcel Regional Characteristics	Alameda	Contra Costa	Marin	Napa	San Francisco	San Mateo	Santa Clara	Solano	Sonoma	Source
join_id										
parcel_id										
county_id										
county										
apn	apn	apn	apn	apn	apn	apn	apn	apn	apn	County assessor derived
jurisdiction	situs_city	situs_city_abbr	situs_city	situs2		situs_city	city_code	site_city	situscity	County assessor derived
building_type	use_code	use_code	use_cd	usecode	 rp1clacde	property_use_code	use_code	use_code	usecode	County assessor derived
building_sqft	building_area	(Calculated Value) building_1_sq_feet + residence_2nd_floor_sq_ft + residence_lower_level_sq_ft	liv_area_sqft			gross_bldg_area	total_area	total_area_of_building	(Calculated Value) buildingprimarysize + buildingsecondarysize	MTC/County Assessor Derived
non_residential_sqft	(Calculated Value) lot_size - building_area	(Calculated Value) area - (building_1_sq_feet + residence_2nd_floor_sq_ft + residence_lower_level_sq_ft)	(Calculated Value) land_sqft - liv_area_sqft		sqft	(Calculated Value) sq_ft_actual - gross_bldg_area	(Calculated Value) usable_sq_feet - total_area	 (Calculated Value) lot_size__sq__ft__ - total_area_of_building	(Calculated Value) landsizesqft - (buildingprimarysize + buildingsecondarysize)	MTC/County Assessor Derived
residential_units	 number_of_units	 total_rooms	 living_units		 units	 no_of_units	 number_units	  number_of_units	  (Calculated Value) buildingprimaryunitcount + buildingsecondaryunitcount	MTC/County Assessor Derived
year_built	year_built	year_built	construct_yr		yr_blt	year_built	year_built	year_built	buildingprimaryyearbuilt	MTC/County Assessor Derived
assessed_building_value	imps	improvement_value	imp_value	currentnetvalue	 rp1impval	improvement_value	securedimprove	improvement_value	 value601netvalue	County assessor derived
assessed_date	doc_dt				 valdate		 date_updated		asmntstatusdate	MTC/County Assessor Derived
last_sale_price	 value_from_trans_tax				 recurrpric	 last_sale_amount			 salesalesprice	MTC/County Assessor Derived
last_sale_date	 transfer_dt			 transferdate	 recurrsald	 date_of_last_sale	 datetransfer		 salerecordingdate	MTC/County Assessor Derived
bedrooms	 number_of_bedrooms	 bedrooms	 nbr_bedrooms		 beds	 __of_bedrooms, __of_bedroom	 bedroom	 number_of_bedrooms, number_of_studio_apts, number_of_one_bedroom_apts, number_of_two_bedroom_apts, number_of_other_type_apts	 buildingprimarybedrooms	MTC/County Assessor Derived
building_height	number_of_stories	(Calculated Value) case when residence_lower_level_sq_ft > 0 then 1 when residence_2nd_floor_sq_ft > 0 then 2 else null end			storeyno	(Calculated Value) case when first_floor_area > 0 then 1 when second_floor_area > 0 then 2 when third_floor_area > 0 then 3 else null end	(Calculated Value) case when first_floor_area > 0 then 1 when second_flr_area > 0 then 2 when third_floor_area > 0 then 3 when number_floors > 0 then number_floors else null end	(Calculated Value) case when area_of_first_floor > 0 then 1 when area_of_second_floor > 0 then 2 when area_of_third_floor > 0 then 3 else null end	buildingprimarystories	MTC/County Assessor Derived
use_code	 use_code	 use_code	 use_cd	usecode	 rp1clacde	property_use_code	use_code	 use_code	usecode	County assessor derived
 use_code_name	 use_code_name								usecodetype	MTC/County Assessor Derived
units	 number_of_units	 total_rooms	 living_units		 units	 no_of_units	 number_units	  number_of_units	  buildingprimaryunitcount, buildingsecondaryunitcount	MTC/County Assessor Derived
bathroom	 number_of_bathrooms	 bathrooms	 nbr_bathrooms		 baths	 __of_bathroom, bathroom, baths	 bath_rooms	 number_of_baths	 buildingprimarybaths	County assessor derived
land_improvement_ratio	 (Calculated Value) land/imps	(Calculated Value) land_value/improvement_value	(Calculated Value) land_value/imp_value	 (Calculated Value) currentmarketlandvalue/currentnetvalue	 (Calculated Value) rp1lndval/rp1impval	(Calculated Value) land_value/improvement_value	(Calculated Value) landvalue/securedimprove	(Calculated Value) land_value/improvement_value	 (Calculated Value) value601land/value601netvalue	
address	(Calculated Value) case(situs_street_number) when null then ''when 'nan' then '' else situs_street_number || ' ' end ||situs_street_name ||case(situs_unit_number) when null then ', 'when 'nan' then ', 'else ', Unit ' || situs_unit_number || ', 'end ||situs_city || ', CA ' || situs_zip_code	(Calculated Value) case(situs_street_nbr) when null then ''when 'nan' then '' else situs_street_nbr || ' ' end ||situs_street_name || ' ' || case(situs_street_suffix) when null then ', 'when 'nan' then ', ' else situs_street_suffix || ', ' end ||situs_city_abbr || ', CA ' || situs_zip	(Calculated Value) case(situs_formatted)when null then ''when 'nan' then ''else situs_formatted || ' ' end ||case(situs_city)when null then ''when 'nan' then ''else situs_city || ', CA' end	(Calculated Value) case(situs1)when null then ''when 'nan' then '' else situs1 || ', ' end ||situs2	address	(Calculated Value) case(situs_no1)when null then ''when 'nan' then '' else situs_no1 || ' ' end ||case(situs_direction)when null then ''when 'nan' then '' else situs_direction || ' ' end ||case(situs_street)when null then ''when 'nan' then '' else situs_street || ' ' end ||case(situs_street_type)when null then ''when 'nan' then '' else situs_street_type || ', ' end ||case(situs_street_box)when null then ''when 'nan' then '' else situs_street_box || ', ' end ||case(situs_city)when null then ''when 'nan' then '' else situs_city || ', CA' end	(Calculated Value) case(house_number)when null then ''when 'nan' then '' else house_number || '' end ||case(house_suffix)when null then ''when 'nan' then '' else house_suffix || ', ' end ||case(unit_number)when null then ''when 'nan' then '' else 'Unit ' || unit_number || ', ' end ||case(street_direction)when null then ''when 'nan' then '' else street_direction || ' ' end ||case(street_name)when null then ''when 'nan' then '' else ' ' || street_name || ' ' end ||case(street_suffix)when null then ''when 'nan' then '' else street_suffix || ', ' end ||case(city_code)when null then ''when 'nan' then '' else city_code || ', CA' end	(Calculated Value) case(situs_street_number)when null then ''when 'nan' then '' else situs_street_number || ' ' end ||case(situs_street_name)when null then ''when 'nan' then '' else situs_street_name || ', ' end ||case(site_building)when null then ''when 'nan' then '' else 'Building ' || site_building || ', ' end ||case(site_unit_)when null then ''when 'nan' then '' else 'Unit ' || site_unit_ || ', ' end ||case(site_city)when null then ''when 'nan' then '' else site_city || ', CA' end	(Calculated Value) case(situsformatted1)when null then ''when 'NONE' then ''else situsformatted1 || ', ' end ||situsformatted2	MTC/County Assessor Derived

### Alameda County

### Contra Costa County

### Marin County

### Napa County

### San Francisco (City and County)

### San Mateo County

### Santa Clara County

### Solano County

### Sonoma County

## Related Works
