# Assessor Parcel Data Characteristics

## Inputs

- Assessor parcel data (various formats): [(Box folder)](https://mtcdrive.app.box.com/folder/74541964646)
	- Note: Original Assessor parcel data documentation is in each county's subfolder (if provided)


## Outputs

**Main output:** Redshift tables with all data for each county
- The resulting county parcel data Redshift tables are currently on the dev database under the basis schema (e.g. basis.alameda_county_characteristics)

**Additional outputs:**
- Step 1 outputs (one csv file for each Assessor data file):

	- Original column names (text file): 
		- Start in the main data processing Box folder (https://mtcdrive.app.box.com/folder/74861288279), go to desired county folder, go to data_features folder, and for each county Assessor data source there will be a text file of original column names
		(e.g. https://mtcdrive.app.box.com/file/447788921368)

	- Standardized data for each source (csv files):
		- Start in the main data processing Box folder (https://mtcdrive.app.box.com/folder/74861288279), go to desired county folder, go to csv_data folder,
		and for each county Assessor data source there will be a csv file
		(e.g. https://mtcdrive.app.box.com/file/447782332655)


- Step 2 outputs (a single csv file per county with all provided Assessor data combined and a data_source column):

	- Combined csv data for each county
		- Start in the main data processing Box folder (https://mtcdrive.app.box.com/folder/74861288279), go to desired county folder, go to csv_data folder, go to step_2_output folder, and there will be a csv file with all Assessor data for the county
		(e.g. https://mtcdrive.app.box.com/file/447780171580)


- Step 3 outputs (Redshift tables of parcel data for each county):

	- Redshift column rename dictionary (json file):
		- Start in the main data processing Box folder (https://mtcdrive.app.box.com/folder/74861288279), go to desired county folder, go to csv_data folder, go to step_2_output folder, and for each county Assessor data source there will be a json file
		(e.g. https://mtcdrive.app.box.com/file/447780513694)

	- Table creation commands (txt file):
		- **NOTE:** This file contains the commands used to create each county's Redshift table, but this file was not actually used to create the table (table was created with in-memory string with the contents of the txt file). The file is for reference only.
		-  Start in the main data processing Box folder (https://mtcdrive.app.box.com/folder/74861288279), go to desired county folder, go to csv_data folder, go to step_2_output folder, and for each county Assessor data source there will be a txt file
		(e.g. https://mtcdrive.app.box.com/file/447787785528)

	- S3 base data (Redshift-ready csv files for each county on S3):
		- The base data for the Redshift tables was written to S3 (https://s3.console.aws.amazon.com/s3/buckets/mtc-basis/?region=us-west-2&tab=overview)

## Data Transformation process:

### I. Write each data file to standard format (csv)

**Start:** file(s) in format given by county assessor

**End:** csv file for each original data source, modified csv file (with building_num if applicable)

**Process:**

1. Initialize column widths dictionary **Note: This step only applies to fixed-width file formats** (e.g. Alameda, )
- copied columns from provided table documentation into excel file
- copied the column name and width columns into Sublime
- did text replace (replace tab with "': ", replace newline with ", '") and copied to Jupyter to create Python dictionary

2. Load data as pandas DataFrame with columns and write to csv (one csv file for each source)
- for fixed-width file format, `process_fwf_data` function in `utils.py`
- for tabular file format, `process_tabular_data` function in `utils.py`

**Notes:** 

Counties with fixed-width file formats: Alameda, San Francisco, San Mateo, Solano

Counties with tabular file formats: Marin, Napa, Santa Clara, Sonoma

3. Data modification: drop duplicates, add building ID for files with buildings records (indicated by duplicate APNs)

### II. Concatenate data to one master file (csv) for each county

**Start:** file(s) in csv format for each data source given by county assessor

**End:** single csv file for each county

**Process:** (`concat_data_add_source` function in `utils.py`)

1. Concatenate (stack) data into a single dataframe
2. Add data_source column attributing county data file source
3. Fill known null APN data, drop duplicate observations, replace values, convert column types

**Notes:** Counties that provided only one data file (Alameda, Marin, Napa, Sonoma) have 'original' as their data_source


### III. Post data to S3 and Redshift

**Start:** single csv file for each county

**End:** Redshift table for each county (currently on *dev* database)

**Process:** (`create_county_redshift_table` function in `utils.py`)

1. Rename column names (to make Redshift-compatible)
2. Push each county's dataframe to S3
3. Initialize tables on Redshift
4. Copy S3 data to Redshift tables 

**Notes:** Not currently on *staging* and *lake* databases 
