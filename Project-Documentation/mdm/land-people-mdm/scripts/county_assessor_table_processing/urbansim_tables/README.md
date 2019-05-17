# Urbansim Table Processing

## Data processing steps:

**Note**: Notebooks with the prefix `DS INPUT` are meant to be used by data stewards. Data steward processing guidelines are outlined at the end of this file.

1. Create basis.parcels_2018 Redshift table from Parcels 2018 data on Socrata
	- `Create_parcels_2018.ipynb`

Pulls the Parcels 2018 data from Socrata and pushes it to S3 and Redshift.

2. Initialize basis.urbansim_buildings and basis.urbansim_parcels Redshift tables
	- `Init_urbansim_tables.ipynb`

Initializes the UrbanSim table schemas and copies joinid, apn, fipco, and jurisdict from basis.parcels_2018 to both tables.

3. Per Urbansim table, create county to urbansim field name mapping for each county **(requires data steward input)**
	- `DS INPUT County Urbansim Parcels Column Mapping Tool.ipynb`
	- `DS INPUT County Urbansim Buildings Column Mapping Tool.ipynb`

The data stewards will use this tool to create column mappings from county columns to UrbanSim columns. The resulting column mappings created by the data steward will be saved for use in the subsequent step.

4. Copy county data with column mapping to basis.urbansim_buildings and basis.urbansim_parcels
	- `Update_urbansim_buildings_county.ipynb`
	- `Update_urbansim_parcels_county.ipynb`

Copies each county's data to the UrbanSim tables on Redshift given the column mappings produced by the data steward in the preceding step.

5. Create Urbansim datasets on Socrata
	- `Create_Socrata_tables.ipynb`

Pulls the UrbanSim tables from Redshift and publishes them to Socrata.

6. Exploratory Data Analysis (EDA) of UrbanSim Tables and proposed data changes **(requires data steward input)**
	- `DS INPUT UrbanSim Dataset Exploration.ipynb`

The data stewards will use this notebook to perform EDA on the UrbanSim tables. Their resulting proposed data updates should be sent to Joshua Croff (jcroff@bayareametro.gov), and the notebook and outputs created by their EDA process should be sent to Kaya Tollas (ktollas@bayareametro.gov) for auditing and implementation. The DataViz team reserves the right to maintain the master copy of the datasets on Socrata, thus all data changes are not official unless vetted and implemented by the DataViz team following the described process.

7. Incorporate data steward feedback into UrbanSim tables, QA/QC
	- `Fix_urbansim_parcels.ipynb`
	- `Fix_urbansim_parcels.ipynb`

Implements data steward feedback, performs data quality checks, and updates Socrata tables accordingly.

## Data Steward Processing Guidelines

All notebooks with the prefix `DS INPUT` are meant to be used by data stewards.

0. Get the `county_assessor_table_processing` folder on your local machine
    - Option A: Make a local copy of this [Box folder](https://mtcdrive.app.box.com/folder/76598831864)
    - Option B:  Clone or download this [Github repository](https://github.com/BayAreaMetro/DataServices). All `DS INPUT` notebooks are in the folder `Project-Documentation/mdm/land-people-mdm/scripts/county_assessor_table_processing/urbansim_tables`
1. Run this notebook and perform your own EDA
2. Save your modified notebook and any outputs in a folder and copy that folder to this [Box folder](https://mtcdrive.app.box.com/folder/76889542701)
3. Communicate your updates to the DataViz team
    - write data-specific notes via BASIS
    - write general communications in the Slack channel #urbansim-data-collab [?] informing the DataViz and UrbanSim teams that you made an update to the Box folder
    - Github issues in this repo: 
