"""
This file contains utility functions for BASIS data processing (I/O, etc.)
"""

import io
import os
import sys
import glob
import json
import numpy as np
import pandas as pd
from sqlalchemy import types
from collections import Counter

# local imports
from config import (step_1_output_dir, csv_dir, columns_dir,
    step_2_output_dir, step_3_output_dir)

user = os.environ['USER']
base_path = '/Users/{}/Box/DataViz Projects/Data Services/BASIS MDM/raw_data/Property and Building Characteristics'.format(user)

sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Application Secure Files/'.format(user))
from creds import (REDSHIFT_USERNAME, REDSHIFT_PSWD,
                         AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Utility Code'.format(user))
from utils_io import *


def init_step_1(county_name, step_1_d, input_dir, init_output_dirs=True):
    """Given a county_name, step_1_d of data_ids and their filenames, and
    the county's Assessor data folder, initializes the inputs and output
    directories for Step I"""
    # if init_output_dirs:
    #     makedirs_if_not_exists(csv_dir)
    #     makedirs_if_not_exists(columns_dir)
    
    for k, v in step_1_d.items():
        input_fname = v['input']
        v['input'] = os.path.join(input_dir, input_fname)
        v['output'] = '{}_Assessor_Data_{}'.format(county_name, k)
    return step_1_d


def write_step_1_data(df, county_name, data_id, step_1_d):
    """Given a pandas DataFrame of Step I data, """

    output_id = step_1_d[data_id]['output']
    # write column names
    columns_fname = '{}_Assessor_cols_{}.txt'.format(county_name, data_id)
    write_lines(df.columns, os.path.join(columns_dir, columns_fname))
    print('column names saved at {}'.format(columns_dir))

    # push data to S3
    s3_fname = os.path.join(county_name, output_id + '.csv')
    s3_bucket = 'mtc-basis'
    s3_key = 'land_people/county_assessor_data/step_1_outputs/{}'.format(s3_fname)
    post_df_to_s3(df, bucket=s3_bucket, key=s3_key)
    print('Step I initial step complete. Output data on S3 at s3://{}/{}\n'.format(s3_bucket, s3_key))


def read_fwf(path, colwidth_dict, **kwargs):
    """Given a data path and column width dictionary, reads
    a fixed-width dataframe and names its columns"""
    df = pd.read_fwf(path,
                     header=None,
                     widths=list(colwidth_dict.values()),
                     **kwargs
                    )
    df.columns = colwidth_dict.keys()
    return df


def process_fwf_data(county_name, data_id, step_1_d, input_dir, colwidths_dict,
    init_output_dirs=True):
    """
    Given the data folder of the county's Assessor Parcel data,
    the fname of the FWF txt file ({fname}.txt), the dictionary of
    column names to widths, and a county name (spaces must be replaced with underscores),
    writes colwidths_dict to {county_name}_{fname}_colwidths.json
    and writes the data to csv. Returns a dictionary with colwidths_fname
    and df_path
    """

    # initialize step 1 output directories
    step_1_d = init_step_1(county_name, step_1_d,
                           input_dir, init_output_dirs)

    
    # write colwidths_dict to file
    colwidths_fname = '{}_{}_colwidths.json'.format(county_name, data_id)
    dump_json(colwidths_dict, os.path.join(columns_dir, colwidths_fname))

    # load with column names
    input_fname = step_1_d[data_id]['input']
    df = read_fwf(input_fname, colwidths_dict)
    # write data
    write_step_1_data(df, county_name, data_id, step_1_d)
    return df


def process_tabular_data(county_name, data_id, step_1_d, input_dir,
    init_output_dirs=True, col_rename_dict=None):
    """Given the data_id (one of the keys in step_1_d), step_1_d (a dictionary of 
    data_ids and their input and output filenames) of a tabular county Assessor data file
    and a county name (spaces must be replaced with underscores),
    writes the data to a csv"""

    # initialize step 1 output directories
    step_1_d = init_step_1(county_name, step_1_d,
                           input_dir, init_output_dirs)

    input_fname = step_1_d[data_id]['input']

    try:
        df = pd.read_csv(input_fname)
    except Exception:
        df = pd.read_excel(input_fname)
    if col_rename_dict is not None:
        df.rename(columns=col_rename_dict, inplace=True)
    # write data
    write_step_1_data(df, county_name, data_id, step_1_d)
    return df


def nan_count(row):
    """Used for dropping duplicate building_id observations with less data"""
    return row.isna().sum()


def zero_count(row):
    """Used for dropping duplicate building_id observations with less data"""
    return (row == '0').sum()


def resolve_building_id(df):
    """Drops duplicate building_id rows from a DataFrame
    with less information (e.g. more Nan and 0 values)"""
    df['building_id'] = ('A' + df['APN'].astype(str)
                          + 'B' + df['BUILDING_NUM'].astype(str))
    vcs = df['building_id'].value_counts()
    dup_ids = vcs[vcs > 1].index
    for building_id in dup_ids:
        # get rows with duplicate building_ids
        rows = df[df['building_id'] == building_id].copy()
        # assess information content of each row
        rows['nan_count'] = rows.apply(nan_count, axis=1)
        rows['zero_count'] = rows.apply(zero_count, axis=1)
        rows['bad_val_count'] = rows['nan_count'] + rows['zero_count']
        # get index of row with the most information
        keep_idx = rows['bad_val_count'].idxmin()
        # drop the others
        drop_rows = set(rows.index).difference(set([keep_idx]))
        df.drop(drop_rows, inplace=True)


def modify_step_1_data(county_name, data_id, df_dict, step_1_d, building_id=True):
    """
    Modifies the output of Step I (csv file for a county data source):

    - drops duplicates
    - if building_id=True, creates unique building_id field
     (drops duplicate building_ids that contain less information)

    NOTE: Currently only tested on Santa Clara"""
    df = df_dict[data_id]
    df.drop_duplicates(inplace=True)
    if building_id:
        resolve_building_id(df)

    output_id = step_1_d[data_id]['output']
    mod_fname = output_id + '_MOD.csv'
    df.to_csv(os.path.join(csv_dir, mod_fname), index=False)
    # push data to S3
    s3_fname = os.path.join(county_name, mod_fname)
    s3_bucket = 'mtc-basis'
    s3_key = 'land_people/county_assessor_data/step_1_outputs/{}'.format(s3_fname)
    post_df_to_s3(df, bucket=s3_bucket, key=s3_key)
    print('Step I complete. Output data in {} and on S3 at s3://{}/{}\n'.format(csv_dir, s3_bucket, s3_key))


def modify_step_2_data(df, replace_d=None, conv_d=None):
    """
    Modifies the concatenated data:

    - drops duplicates
    - optionally replaces values with given replace_d
    - replace null values (resulting from different data sources not duplicating
    main APN data) for each APN with known APN values
    - optionally converts data types with given conv_d


    Warning: For filling null APN data, originally had

    def fillna(df):
        return df.fillna(method='ffill').fillna(method='bfill')
    df = df.groupby('APN').apply(fillna)

    but it took FOREVER, didn't complete, and had to be killed eventually.

    Instead followed this approach: https://stackoverflow.com/a/36288458
    """
    print('data shape before dropping duplicates: {}'.format(df.shape))
    df.drop_duplicates(inplace=True)
    print('data shape after dropping duplicates: {}'.format(df.shape))
    if replace_d is not None:
        df.replace(replace_d, inplace=True)
        for k, v in replace_d.items():
            print('replaced {} with {}'.format(k, v))
    
    # fill null values with known APN values
    # significantly sped up with this approach: https://stackoverflow.com/a/36288458
    g = df.groupby('APN', sort=False).first()
    fillna_cols = set(df.columns).difference(['APN', 'building_id'])
    for c in fillna_cols:
        df[c] = df['APN'].map(g[c])
    if conv_d is not None:
        for c, new_dtype in conv_d.items():
            if df[c].dtype == float and new_dtype == str:
                df[c] = df[c].astype(str).str.strip('.0')
            else:
                df[c] = df[c].astype(new_dtype)
            print('converted column {} to {} type'.format(c, new_dtype))
    return df


def concat_data_add_source(county_name, replace_d=None, conv_d=None):
    """
    Step II of County Assessor Data standardization process.

    Given a county's csv output folder from Step I of data processing,
    concatenates the data in the output csv files and adds source.
    Final data file is called <county>_Assessor_Data.csv

    This function is used for data files that have no shared columns
    """

    # initialize step 2 output directory
    output_dir = step_2_output_dir
    makedirs_if_not_exists(output_dir)

    csv_folder = 'step_1_outputs/csv_data'
    df_paths = glob.glob(os.path.join(csv_folder, '*.csv'))
    dfs = {}
    if len(df_paths) == 0:
        print('no csv files in this folder')
        return
    for df_path in df_paths:
        # base_fname is of format <county_name>_Assessor_Data<_optional_source if in multiple files>
        base_fname = os.path.splitext(os.path.split(df_path)[-1])[0]
        df_source = '_'.join(base_fname.split('_')[3:])
        df = pd.read_csv(df_path)
        # add data source as column
        # 'source' threw Redshift error for San Francisco since that column already existed
        df['data_source'] = df_source
        dfs[df_source] = df
    concat_df = pd.concat(dfs.values(), sort=False)

    df = modify_step_2_data(concat_df, replace_d=replace_d, conv_d=conv_d)

    # write output
    output_fname = '{}_Assessor_Data.csv'.format(county_name)
    output_name = os.path.join(output_dir, output_fname)
    df.to_csv(output_name, index=False)
    print('final csv file at {}'.format(output_name))

    # push data to S3
    s3_bucket = 'mtc-basis'
    s3_key = 'land_people/county_assessor_data/step_2_outputs/{}'.format(output_fname)
    post_df_to_s3(df, bucket=s3_bucket, key=s3_key)
    print('Step II complete. Output data in {} and on S3 at s3://{}/{}'.format(output_dir, s3_bucket, s3_key))


def find_duplicate_cols():
    """
    Precursor to Step III: read the combined csv from step_2_outputs
    and find the columns that cause

    <ProgrammingError: column "{bad column name}" duplicated error>

    at Step III (create_county_redshift_table)
    """
    # there is a single combined csv in this folder
    step_2_output_fname = glob.glob(os.path.join(step_2_output_dir, '*.csv'))[0]
    df = pd.read_csv(step_2_output_fname, nrows=10)

    lowercase_cols = [c.lower() for c in df.columns]

    col_counter = Counter(lowercase_cols)
    dup_cols = []
    for k, v in col_counter.items():
        if v > 1:
            dup_cols.append(k)
    return dup_cols


def create_county_redshift_table(county_name, ctype_override=None):
    """
    Step III of County Assessor Data standardization process.

    Creates a redshift table named basis.<county_name>_county
    and copies csv files to S3 bucket mtc-basis
    """

    # initialize step 3 output directory
    output_dir = step_3_output_dir
    makedirs_if_not_exists(output_dir)

    # initialize output names
    s3_bucket = 'mtc-basis'
    s3_key = 'land_people/county_assessor_data/step_3_outputs/{}_Assessor_Data_Redshift.csv'.format(county_name)
    # tablename must be lowercase for post_df_as_redshift_table to overwrite
    # otherwise throws error if table already exists
    tablename = 'basis.{}_county'.format(county_name).lower()

    # read output of Step II
    df_path = os.path.join(step_2_output_dir, '{}_Assessor_Data.csv'.format(county_name))
    df = pd.read_csv(df_path)

    # make column names Redshift-compatible
    redshift_colname_map = create_redshift_colname_map(df)
    df.rename(columns=redshift_colname_map, inplace=True)
    colname_map_fname = os.path.join(output_dir,
                                     '{}_colname_map_Redshift.json'.format(county_name))
    dump_json(redshift_colname_map, colname_map_fname)

    # initialize table data schema
    column_type_dict = create_redshift_column_type_dict(df)
    # ensure that apn is string type
    apn_col = [c for c in df.columns if 'apn' in c.lower()][0]
    if apn_col in df._get_numeric_data():
        column_type_dict['APN'] =  types.VARCHAR(100)
        # trim .0
        df[apn_col] = df[apn_col].astype(str).str.strip('.0')

    if ctype_override is not None:
        for column, dtype in ctype_override.items():
            if column in column_type_dict:
                column_type_dict[column] = dtype

    # only creating for documentation purposes. Actual table creation is called in
    # create_redshift_table_via_s3 function below
    table_schema_str = create_redshift_table_str(tablename, column_type_dict)
    table_schema_fname = os.path.join(output_dir,
                                     '{}_table_init_Redshift.sql'.format(county_name))
    write_text(table_schema_str, table_schema_fname)

    # push data to S3
    post_df_to_s3(df, bucket=s3_bucket, key=s3_key)
    # create Redshift table from S3 data
    s3_path = os.path.join('s3://', s3_bucket, s3_key)
    # this function calls create_redshift_table_str on the column_type_dict
    create_redshift_table_via_s3(tablename, s3_path, dbname='dev',
                                 column_type_dict=column_type_dict, overwrite=True)
