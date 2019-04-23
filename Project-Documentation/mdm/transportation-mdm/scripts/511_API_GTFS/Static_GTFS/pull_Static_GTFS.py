"""Given the GTFS_FILES and OPERATOR_ID_MAP in config.py, this python
script downloads GTFS data for each operator from the 511 api and for
each expected GTFS file (from GTFS_FILES), concatenates GTFS data from
all operators into an output file, e.g. stops_all_agencies.csv

REQUIRED:
The variables DEV_511_API_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
REDSHIFT_USERNAME, and REDSHIFT_PSWD need to be set in the environment
prior to running this script.

Recommended: set these variables in ~/licenses/set_creds.sh

Run with:

source ~/licenses/set_creds.sh
python ingest_511_GTFS.py
"""

import os
import sys
import time
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

# local imports
from config import GTFS_FILES, gtfs_type_dict

import sys
sys.path.insert(0, '../')
from utils import (init_logger, print_runtime, post_df_to_s3,
 create_redshift_table_via_s3, post_df_as_redshift_table)
from 511_config import OUTPUT_DIR, OPERATOR_ID_MAP


def pull_511_gtfs_static(to_redshift=True, to_csv=True):
    """For each agency in OPERATOR_ID_MAP, pulls all files specified
    by GTFS_FILES in config.py into memory and joins them into a a
    single pandas DataFrame for each GTFS file. If to_redshift is True,
    writes each dataframe to a Redshift table (Redshift DB
    specifications are in utils and config). If to_csv is True, writes
    each dataframe to a csv file, otherwise returns a dictionary with
    the following format:

    {GTFS_file: dataframe of concatenated GTFS_file from all acencies, ...}

    e.g. {'agency.txt': <pandas DataFrame of concatenated agency.txt
    files from all agencies>,
          'calendar.txt': ..., ...}
    """
    # initialize logger
    logger = init_logger('gtfs_static_pull', OUTPUT_DIR)
    a = time.time()
    # initialize empty dictionary of GTFS file: list of dataframes (one 
    # for each operator)
    GTFS_df_dict = dict(zip(GTFS_FILES, [[] for f in GTFS_FILES]))

    API_511_base = 'http://api.511.org/transit/datafeeds?'

    for operator_id, operator_name in OPERATOR_ID_MAP.items():
        request_url = API_511_base + 'api_key={}&operator_id={}'.format(DEV_511_API_KEY, operator_id)
        resp = urlopen(request_url)
        # read zipfile into memory 
        operator_GTFS_zipfile = ZipFile(BytesIO(resp.read()))
        for GTFS_file in GTFS_FILES:
            try:
                # load .txt file contained in zipfile into DataFrame
                df = pd.read_csv(operator_GTFS_zipfile.open(GTFS_file))
                # add ids if not present in GTFS
                if 'agency_id' not in df.columns:
                    df['agency_id'] = operator_id
                if 'agency_name' not in df.columns:
                    df['agency_name'] = operator_name
                GTFS_df_dict[GTFS_file].append(df)
            except Exception as e:
                logger.info('failed to pull {} for {}'.format(GTFS_file, operator_id))
                logger.info(e)

    # build final dictionary: {filename: dataframe with all agencies, ...}
    for k, v in GTFS_df_dict.items():
        # concatenate list of dataframes to single dataframe
        GTFS_df_dict[k] = pd.concat(v, ignore_index=True)
        # e.g. k='calendar.txt' -> table_name = gtfs_calendar
        tablename = 'gtfs_' + os.path.splitext(k)[0]
        # if writing to Redshift tables, create a table for each filename in the GTFS feed 
        if to_redshift:
            c = time.time()
            # these GTFS tables have lots of rows (>20k)
            # post them to S3 and create Redshift table from S3
            if k in ['stop_times.txt', 'stops.txt', 'trips.txt']:
                s3_key = 'GTFS_files/{}.csv'.format(tablename)
                post_df_to_s3(GTFS_df_dict[k], bucket='rtd-archives', key=s3_key)
                s3_path = 's3://rtd-archives/GTFS_files/{}.csv'.format(tablename)
                create_redshift_table_via_s3(tablename, s3_path, gtfs_type_dict[tablename])
            else:
                continue
                # post_df_as_redshift_table(tablename, GTFS_df_dict[k], dtypes=gtfs_type_dict[tablename])
            d = time.time()
            logger.info('table created on Redshift: {}. Took {}'.format(tablename, print_runtime(d-c)))
        # if writing to csv files, create a csv for each filename in the GTFS feed 
        if to_csv:
            output_fname = tablename + '.csv'
            # write to output directory
            output_dir = os.path.join(OUTPUT_DIR, 'gtfs_static_pull')
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_fname = os.path.join(output_dir, output_fname)
            GTFS_df_dict[k].to_csv(output_fname, index=False)
            # print('output created at {}'.format(output_fname))
            logger.info('output created at {}'.format(output_fname))
    b = time.time()
    logger.info('GTFS static pull took {}'.format(print_runtime(b-a)))
    # if not writing to csv files, return the final dictionary
    if not to_csv:
        return GTFS_df_dict


def get_operator_ids_from_511(append_to_config=True):
    """Given a 511 API key, downloads a dictionary of operator ID
    (acronym) to operator name. This function is a combination of
    get_511_orgs_dict and get_org_acronyms_from_511 from
    https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/rtd/etl/get_511_current_gtfs_metadata_and_gtfs.py  # noqa
        
    NOTE: Currently pulls more agencies than specified in
    OPERATOR_ID_MAP from config.py:
    
    Example:
    
    from config import OPERATOR_ID_MAP
    
    pulled_ids = get_org_acronyms_from_511()
    set(pulled_ids.keys()).difference(set(OPERATOR_ID_MAP.keys()))
    {'5E', '5F', '5O', '5S', 'NV', 'SS'}
    
    (which corresonds to ['511 Emergency', '511 Flap Sign', '511 Operations',
    '511 Staff', 'Vine (Napa County)', 'Free South City Shuttle'])
    """
    # Pre-requisite
    # ! pip install xmltodict
    import xmltodict
    operator_url = 'http://api.511.org/transit/operators?api_key={}&Format=XML'.format(DEV_511_API_KEY)
    j = requests.get(operator_url)
    d = xmltodict.parse(j.content)
    orgs_list = d['siri:Siri']['siri:ServiceDelivery']['DataObjectDelivery']['dataObjects']['ResourceFrame']['organisations']['Operator']
    operator_ids = {}
    for org in orgs_list:
        operator_ids[org['PrivateCode']] = org['Name']
    # if append_to_config:
    return operator_ids


if __name__ == '__main__':
    # set necessary variables
    DEV_511_API_KEY = os.environ['DEV_511_API_KEY']
    # operator_ids = get_operator_ids_from_511()
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    pull_511_gtfs_static()
   

