# County Assessor Data Processing

This folder contains the scripts that run two phases of County Assessor Data Processing:

## 1. County Tables

**Start:** original county assessor data files

**End:** Redshift table for each county, all output data on S3

## 2. Urbansim Tables

**Start:** original county assessor data files, Parcels 2018 data on Socrata

**End:** Urbansim tables (buildings, parcels) on Redshift and Socrata, all output data on S3