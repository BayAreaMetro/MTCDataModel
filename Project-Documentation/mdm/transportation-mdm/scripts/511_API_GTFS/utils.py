

"""
This file contains utility functions for Transit Data Processing,
such as logging, file I/O, moving data to AWS, etc.

"""

import io
import os
import sys
# Pre-requisite: ! pip install boto3
import boto3
import logging
# Pre-requisite: ! conda install -y -c anaconda psycopg2
import psycopg2
import pandas as pd
# Pre-requisite: ! pip install sqlalchemy-redshift
from sqlalchemy import create_engine

# local imports

# sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'creds'))
# sys.path.insert(0, r'~/Box/DataViz\ Projects/Application\ Secure\ Files/511_GTFS/')

user = os.environ['USER']
sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Application Secure Files/511_GTFS'.format(user))
from credentials import (REDSHIFT_USERNAME, REDSHIFT_PSWD,
 AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Utility Code'.format(user))
from utils_io import *


def init_logger(logger_name, output_dir):
    """Given a logger_name and output_dir, sets the logging level to
    INFO and initializes logger to log to output_dir/<logger_name>.log
    and the console"""
    logger = logging.getLogger(logger_name)
    # otherwise this step fails
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_fname = os.path.join(output_dir, '{}.log'.format(logger_name))
    fileHandler = logging.FileHandler(log_fname)
    logger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    logger.addHandler(consoleHandler)
    logger.setLevel(logging.INFO)
    return logger


def print_runtime(run_seconds):
    """Given a float of runtime seconds, formats the time for more readable logging"""
    if run_seconds > 60:
        mins = run_seconds/60.0
        if mins < 60:
            return '{} minutes'.format(round(mins, 4))
        else:
            return '{} hours'.format(round(mins/60.0, 4))
    else:
        return '{} seconds'.format(round(run_seconds, 4))


def post_df_to_s3(df, bucket, key, split_header=False):
    """
    Given a pandas DataFrame, S3 bucket name, and S3 dest filename,
    posts a dataframe as a csv in S3.

    This function is from https://stackoverflow.com/a/40615630
    """
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())
    print('dataframe on S3 at {}:{}'.format(bucket, key))


def download_df_from_s3(bucket, key):
    """Given an S3 bucket and filename of a table on S3, downloads the
    file as a pandas DataFrame"""
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    return df


def create_redshift_engine():
    """Creates a default Redshift SQLAlchemy engine for pandas-Redshift connections"""
    redshift_host = 'data-viz-cluster.cepkffrgvgkl.us-west-2.redshift.amazonaws.com'

    redshift_connection_params = {'user': REDSHIFT_USERNAME,
                                  'password': REDSHIFT_PSWD,
                                  'port': 5439,
                                  'host': redshift_host,
                                  'dbname': 'dev'}

    psql_engine_str = 'redshift+psycopg2://{}:{}@{}:{}/{}'.format(redshift_connection_params['user'],
                                                             redshift_connection_params['password'],
                                                             redshift_connection_params['host'],
                                                             redshift_connection_params['port'],
                                                            redshift_connection_params['dbname'])

    engine = create_engine(psql_engine_str, echo=True)
    return engine


def post_df_as_redshift_table(tablename, df, dtypes=None):
    """Given a tablename, pandas DataFrame, and optionally a dictionary
    of table columns to sqlalchemy dtypes, writes the DataFrame as a
    Redshift table

    Resource: http://measureallthethin.gs/blog/connect-python-and-pandas-to-redshift/  # noqa
    """
    engine = create_redshift_engine()
    to_Redshift_args = {'name': tablename,
                        'schema': 'transportation',
                        'con': engine,
                        'index': False,
                        'if_exists': 'replace'}
    if dtypes is not None:
        to_Redshift_args['dtype'] = dtypes
    df.to_sql(**to_Redshift_args)


def pull_df_from_redshift_sql(sql_statement):
    """Connects to the default Redshift engine and returns a
    dataframe based on the SQL statement"""
    engine = create_redshift_engine()
    return pd.read_sql(sql_statement, engine)


def create_redshift_table_str(tablename, column_type_dict):
    """Given a tablename (can be schema.tablename), dictionary of column
    name to sqlalchemy type, and optionally a list of non-nullable column names,
    returns a create table statement string for Redshift"""
    table_create_str = 'create table {}('.format(tablename)
    for k, v in column_type_dict.items():
        ctype = str(v)
        # INTEGER and FLOAT
        if 'INTEGER' in ctype:
            ctype = 'INTEGER'
        if 'FLOAT' in ctype:
            ctype = 'FLOAT'
        col_type = '\n{} {},'.format(k, ctype.lower())
        table_create_str += col_type
    # remove final comma
    table_create_str = table_create_str[:-1] + ');'
    return(table_create_str)


def create_redshift_table_via_s3(tablename, s3_path, column_type_dict):
    """
    Inspect table creation errors like this:
    
    SELECT * from stl_load_errors
    WHERE filename LIKE '%GTFS_files/gtfs_%'
    ORDER BY starttime DESC;
    """
    redshift_host = 'data-viz-cluster.cepkffrgvgkl.us-west-2.redshift.amazonaws.com'
    redshift_connection_params = {'user': REDSHIFT_USERNAME,
                                  'password': REDSHIFT_PSWD,
                                  'port': 5439,
                                  'host': redshift_host,
                                  'dbname': 'dev'}
    conn = psycopg2.connect(**redshift_connection_params)
    cur = conn.cursor()
    drop_table_if_exists_command = 'drop table if exists {}'.format(tablename)
    create_table_command = create_redshift_table_str(tablename, column_type_dict)
    copy_data_command = """copy {}
                    from '{}'
                    credentials 'aws_access_key_id={};aws_secret_access_key={}'
                    ignoreheader 1
                    csv;""".format(tablename, s3_path, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    for cmd in [drop_table_if_exists_command, create_table_command, copy_data_command]:
        print(cmd + '\n')
        cur.execute(cmd)
    conn.commit()
    print('table created on Redshift: {}'.format(tablename))


def timedelta_to_time_period_str(timedelta):
    """Given a pandas Timedelta object, returns a string of format
    HH:MM:SS"""
    return str(timedelta).split('days ')[-1]


def timedelta_to_hour_str(td):
    """Returns the hour and minutes from a pandas Timedelta"""
    td_comps = td.components
    return str(td_comps[1]).zfill(2) + ':' + str(td_comps[2]).zfill(2)


def time_period_str_to_timedelta(time_str, start=True):
    """Given a string of format HH:MM format, returns a pandas Timedelta
    object"""
    if start:  # mark start seconds as 00
        time_str += ':00'
    else:  # mark end seconds as 59
        time_str += ':59'
    return pd.Timedelta(time_str)


def read_lines(fname):
    with open(fname) as f:
        data = f.read()
    return data.split('\n')
    

def write_lines(lines, fname):
    """Given an iterable and filename, writes each item as a line to the file"""
    with open(fname, 'w') as f:
        for l in lines:
            f.write(l + '\n')


def load_json(fname):
    """Given a filename, loads the content as a json object"""
    with open(fname) as f:
        obj = json.load(f)
    return obj


def dump_json(obj, fname):
    """Given a json object and a filename, writes the object to the file"""
    with open(fname, 'w') as f:
        json.dump(obj, f)


