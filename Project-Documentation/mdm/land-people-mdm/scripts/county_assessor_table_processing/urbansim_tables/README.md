# Urbansim Table Processing

## Data processing steps:

1. Create basis.parcels_2018 Redshift table from Parcels 2018 data on Socrata
	- `Create_parcels_2018.ipynb`

Pulls the Parcels 2018 data from Socrata and pushes it to S3 and Redshift.

2. Initialize basis.urbansim_buildings and basis.urbansim_parcels Redshift tables
	- `Init_urbansim_tables.ipynb`

Initializes the UrbanSim table schemas and copies joinid, apn, fipco, and jurisdict from basis.parcels_2018 to both tables.

3. Per Urbansim table, create county to urbansim field name mapping for each county **(requires data steward input)**
	- `County Urbansim Parcels Column Mapping Tool.ipynb`
	- `County Urbansim Buildings Column Mapping Tool.ipynb`

The data steward will use this tool to create column mappings from county columns to UrbanSim columns. The resulting column mappings created by the data steward are saved for use in the subsequent step.

4. Copy county data with column mapping to basis.urbansim_buildings and basis.urbansim_parcels
	- `Update_urbansim_buildings_county.ipynb`
	- `Update_urbansim_parcels_county.ipynb`

Copies each county's data to the UrbanSim tables on Redshift given the column mappings produced by the data steward in the preceding step.

5. Create Urbansim datasets on Socrata
	- `Create_Socrata_tables.ipynb`

Pulls the UrbanSim tables from Redshift and publishes them to Socrata.

6. Exploratory Data Analysis (EDA) of UrbanSim Tables and proposed data changes**(requires data steward input)**
	- `UrbanSim Dataset Exploration.ipynb`

The data steward will use this notebook to perform EDA on the UrbanSim tables. Their resulting proposed data updates should be sent to Joshua Croff (jcroff@bayareametro.gov), and the notebook and outputs created by their EDA process should be sent to Kaya Tollas (ktollas@bayareametro.gov) for auditing and implementation. The DataViz team reserves the right to maintain the master copy of the datasets on Socrata, thus all data changes are not official unless vetted and implememted by the DataViz team following the described process.

7. Data cleaning on UrbanSim tables, QA/QC
	- `Fix_urbansim_parcels.ipynb`
	- `Fix_urbansim_parcels.ipynb`

Evaluates the UrbanSim tables for data inconsistencies, duplicates, etc. and fixes them accordingly.
