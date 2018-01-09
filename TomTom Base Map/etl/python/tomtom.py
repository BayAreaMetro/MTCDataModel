#environment - arcpy pro 2 - python 3
import json
import arcpy
import os, glob
import pandas as pd

DATADIR = 'C:/projects/DataServices/TomTom Base Map/large_files/2016_12'
METADATA_CSV = "../metadata/2016_input_data_dictionary.csv"
OUTPUT_SCHEMA = "C:/projects/DataServices/TomTom Base Map/etl/metadata/2015_output_schema.json"
METADATA_JSON = "C:/projects/DataServices/TomTom Base Map/etl/metadata/2016_input_data_dictionary_filenames.json"

def search_for_files(abbrv,file_ending):
    """
    todo: write tests
    """
    searchterm = "**/*_____" + abbrv + file_ending
    filenames = glob.glob(searchterm, recursive=True)
    return(filenames)

def inventory_files(datadir=DATADIR,metadata_csv=METADATA_CSV):
    """
    todo: 
    -consider moving IO operations out of function
    write test that:
    -the dict returned is not empty, contains some files
    -the metadata csv is not empty
    - one of the abbrev's returns a filename that we expect
    """
    import os
    df_meta = pd.read_csv(metadata_csv)
    d_meta = df_meta.to_dict(orient="records")
    os.chdir(datadir)
    for idx, record in enumerate(d_meta):
        if record['feature_type'] in ('Line','Polygon','Point'):
            d_meta[idx]['filenames'] = search_for_files(
                                        record['abbrv'].lower(),
                                        file_ending=".shp")
            #gdbname1 = datadir + "/output/temp.gdb"
            #shp_to_gdb(record['feature_type'],gdbname1) - crashing arcpy-cause might be fc's starting with integer?
        elif record['feature_type'] == "Table":
            d_meta[idx]['filenames'] = search_for_files(
                                        record['abbrv'].lower(),
                                        file_ending=".dbf")
    return(d_meta)

def load_file_to_gdb():

def load_files_to_gdbs(file_inventory, output_schema=OUTPUT_SCHEMA):

def main():
    d = inventory_files()
    with open(METADATA_JSON, 'w') as f:
        json.dump(d, f, indent=4, sort_keys=True)

def shp_to_gdb(filenames,gdbname):
    """
    example: arcpy.FeatureClassToGeodatabase_conversion(Input_Features="'C:/projects/DataServices/TomTom Base Map/large_files/2016_12/nam2016_12/shpd/mn/uc1/usauc1___________oa02.shp'", Output_Geodatabase="C:/projects/DataServices/TomTom Base Map/large_files/2016_12/output/temp.gdb")
    """
    #
    arcpy.conversion.FeatureClassToGeodatabase(
        Input_Features=filenames,
        Output_Geodatabase=gdbname)
    print("loaded {} to {}".format(filenames,gdbname))

def table_to_gdb(filenames,gdbname):
    arcpy.conversion.TableToGeodatabase(
        Input_Features=filenames,
        Output_Geodatabase=gdbname)
    print("loaded {} to {}".format(filenames,gdbname))

if __name__ == "__main__":
    main()