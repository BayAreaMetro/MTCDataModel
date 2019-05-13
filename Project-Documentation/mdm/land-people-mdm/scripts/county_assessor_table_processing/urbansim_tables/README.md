# Urbansim Table Processing

## Data processing steps:

1. Create basis.parcels_2018 Redshift table from Parcels 2018 data on Socrata
2. Initialize basis.urbansim_buildings and basis.urbansim_parcels Redshift tables
3. Copy data from basis.parcels_2018 to basis.urbansim_buildings and basis.urbansim_parcels
4. Get county to urbansim field name mapping for each county ()