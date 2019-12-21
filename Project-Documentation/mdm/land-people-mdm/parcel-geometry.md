-- Draft --

# Parcel Geometry

Processing county source parcel geometries into a cleaned regional schema

### Project Resources

- [Initial parcel geoprocessing documentation](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Parcel)


## Data Sources

- [Downloaded source files (Box folder)]()


## Regional Schema

**Field**|**Data type**|**Notes**
-----|-----|-----
county (FK)|int|DOMAIN: 1,13,41,55,75,85,95,97
city (FK)|varchar(50)|DOMAIN: MTC domain of 109 jurisdictions
parcel\_id (PK)|varchar(100)|Of format '{county prefix}\_{apn}'; this will be used instead of joinid
geom\_id (FK)|varchar(max)|Hashed WKT representation of the parcel centroid
apn (FK)|varchar(100)|Postprocessed MTC APN (with documented field length -- matches processed apn from PRC (parcel regional characteristics)
apn\_raw|varchar(100)|County source APN
centroid\_x|float|Centroid on surface (if concave polygon)
centroid\_y|float|Centroid on surface (if concave polygon)
parcel\_type|int|DOMAIN: water/air, condo/bldg, ROW/common area parcels -- will map these to integer domain
acres|float| 

## Data Processing Steps

**Notes**  
- Raw Collected source files are kept on the BASIS Data Collection Box Folder
- Processed Data is then stored on Redshift (Staging) for QA/QC
- Final Output Tables will be stored on Redshift (Production) and Socrata (DaaS) for sharing and dissemination


**Step 1. Preprocess Parcels**
- See [Parcels 2019 Documentation (GitHub Repo)](https://github.com/BayAreaMetro/Spatial-Analysis-Mapping-Projects/tree/master/Project-Documentation/Parcel)
	- Data is collected and stored in FGDBs (reprojected to WGS 1984/ EPSG 4326) on Box (Data Collection)
		- TODO: Locate them and move there if not already done; also link in Data Sources section
	- There are several geoprocessing steps that will be documented on the GIS Side
		- Geo-processing: centroids, acreage
			- parcel_type: water parcels, -- maybe more
			- city
				- Parcels should have city names -- match to MTC jurisdictions
				- Possible staged process: If null, match (by county + APN) to assessor data and use assessor-provided city. If no match or still null, assign jurisdiction via centroid using our Jurisdiction Boundary dataset
- Output geoprocessed parcels (by county) to geoserver


**Step 2. Clean parcels, put in regional schema on Staging**
- Read semi-processed source data by county from geoserver
- Map to regional schema
- Dedup/ Check APN Formatting: Fix APNs following defined APN formats by county
- Iterate data fixes (tables on Staging)
	- QA/QC dashboard (Compare Assessor Tables to parcels by year)


**Step 3. Publish final parcels (Parcels 2010, 2018, 2019)**
- Copy final Parcels from Staging to Lake
- Join back geometry field and publish to AGOL/Socrata
	- by county - AGOL
	- regional - Socrata


## Results

(on Socrata)

- [Parcels 2010]()
- [Parcels 2018]()
- [Parcels 2019]()

## Tags

parcels, parcels_2010, parcels_2018, parcels_2019
