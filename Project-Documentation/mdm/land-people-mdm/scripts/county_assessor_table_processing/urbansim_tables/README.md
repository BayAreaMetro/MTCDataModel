# Urbansim Table Processing

## Data processing steps:

1. Create basis.parcels_2018 Redshift table from Parcels 2018 data on Socrata
	- `Create_parcels_2018.ipynb`
2. Initialize basis.urbansim_buildings and basis.urbansim_parcels Redshift tables
	- `Init_urbansim_tables.ipynb`
3. Copy data from basis.parcels_2018 to basis.urbansim_buildings and basis.urbansim_parcels
	- `Update_urbansim_buildings_county.ipynb`
	- `Update_urbansim_parcels_county.ipynb`
4. Per Urbansim table, create county to urbansim field name mapping for each county (requires data user input)
	- `County Urbansim Parcels Column Mapping Tool.ipynb`
	- `County Urbansim Buildings Column Mapping Tool.ipynb`
5. Create Urbansim datasets on Socrata
	- `Create_Socrata_tables.ipynb`