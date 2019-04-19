"""Given the GTFS_FILES and OPERATOR_ID_MAP in config.py, this python
script downloads GTFS data for each operator from the 511 api and for
each expected GTFS file (from GTFS_FILES), concatenates GTFS data from
all operators into an output file, e.g. stops_all_agencies.csv

Run with:

python ingest_511_GTFS.py
"""

import os
import sys
import time
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
# Pre-requisite: ! pip install --upgrade gtfs-realtime-bindings
from google.transit import gtfs_realtime_pb2

# local imports
from utils import init_logger, print_runtime, post_df_as_redshift_table
from config import OUTPUT_DIR, GTFS_FILES, OPERATOR_ID_MAP, gtfs_type_dict

sys.path.insert(0, '/Users/ktollas/licenses')
from credentials import DEV_511_API_KEY


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
            ###### WARNING: Since df.to_sql is slow for big data, have to post larger
            ### dataframes to S3 first for the following GTFS tables:
            ### stop_times (2,797,952 rows), stops (21,856 rows)
            post_df_as_redshift_table(tablename, GTFS_df_dict[k], dtypes=gtfs_type_dict[tablename])
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


def pull_511_FeedMessage_realtime(operator_id, source='TripUpdates'):
    """Given an operator_id and source (either 'TripUpdates' or 'VehiclePositions'),
    pulls from the source feed from the 511 API and returns a gtfs_realtime_pb2.FeedMessage"""
    API_511_base = 'http://api.511.org/Transit/{}?'.format(source)
    operator_url = API_511_base + 'api_key={}&agency={}'.format(DEV_511_API_KEY, operator_id)
    # initialize Protocol Buffer
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urlopen(operator_url)
    feed.ParseFromString(response.read())
    return feed


def pull_agency_VehiclePositions_real_time(operator_id):
    """
    Given an operator_id, pulls all real-time vehicle stops as a pandas
    DataFrame
    """
    def extract_vehicle_position_update(entity):
        """Given a gtfs_realtime_pb2.FeedEntity object, returns a
        dictionary of vehicle position updates"""
        vehicle_position_update = {}
        vehicle_position_update['vehicle_id'] = entity.id
        vehicle_position_update['trip_id'] = entity.vehicle.trip.trip_id
        vehicle_position_update['latitude'] = entity.vehicle.position.latitude
        vehicle_position_update['longitude'] = entity.vehicle.position.longitude
        vehicle_position_update['timestamp'] = entity.vehicle.timestamp
        return vehicle_position_update

    # API_511_base = 'http://api.511.org/Transit/VehiclePositions?'
    # operator_url = API_511_base + 'api_key={}&agency={}'.format(DEV_511_API_KEY, operator_id)
    # # initialize Protocol Buffer
    # feed = gtfs_realtime_pb2.FeedMessage()
    # response = urlopen(operator_url)
    # feed.ParseFromString(response.read())

    feed = pull_511_FeedMessage_realtime(operator_id, source='VehiclePositions')
    
    vehicle_positions = [extract_vehicle_position_update(e) for e in feed.entity]
    final_veh_df = pd.DataFrame(vehicle_positions)
    final_veh_df['agency_id'] = operator_id
    return final_veh_df


def pull_VehiclePositions_real_time(to_csv=True):
    """Calls pull_agency_VehiclePositions_real_time for each agency in
    OPERATOR_ID_MAP. Returns a dataframe of all real-time TripUpdates
    (including departure_time, stop_id) of AVL
    vehicles for each agency"""

    # initialize logger
    logger = init_logger('gtfs_real_time_VehiclePositions_pull', OUTPUT_DIR)

    a = time.time()
    vehicle_pos_dfs = []
    for operator in OPERATOR_ID_MAP.keys():
        try:
            veh_pos_df = pull_agency_VehiclePositions_real_time(operator)
            vehicle_pos_dfs.append(veh_pos_df)
        except Exception as e:
            # print('failed to pull VehiclePositions for {}'.format(operator))
            # print(e)
            logger.info('failed to pull VehiclePositions for {}'.format(operator))
            logger.info(e)
    final = pd.concat(vehicle_pos_dfs, ignore_index=True)
    final['agency_name'] = final['agency_id'].map(OPERATOR_ID_MAP)
    b = time.time()
    logger.info('GTFS real time VehiclePositions pull took {}'.format(print_runtime(b-a)))
    if to_csv:
        # write to output directory
        output_dir = os.path.join(OUTPUT_DIR, 'gtfs_real_time_pull')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_fname = os.path.join(output_dir, 'VehiclePositions_real_time.csv')
        final.to_csv(output_fname, index=False)
        logger.info('output created at {}'.format(output_fname))
        # print('output created at {}'.format(output_fname))
    # if not writing to csv files, return the final DataFrame
    else:
        return final


def pull_agency_TripUpdates_real_time(operator_id):
    """
    Given an operator_id, pulls all real-time vehicle stops as a pandas
    DataFrame.
    """

    def extract_stop_time_update(stop):
        """Given a gtfs_realtime_pb2.StopTimeUpdate object, returns a
        dictionary of stop time updates"""
        stop_update = {}
        stop_update['departure_time'] = stop.departure.time
        stop_update['stop_id'] = stop.stop_id
        return stop_update

    # API_511_base = 'http://api.511.org/Transit/TripUpdates?'
    # operator_url = API_511_base + 'api_key={}&agency={}'.format(DEV_511_API_KEY, operator_id)
    # # initialize Protocol Buffer
    # feed = gtfs_realtime_pb2.FeedMessage()
    # response = urlopen(operator_url)
    # feed.ParseFromString(response.read())

    feed = pull_511_FeedMessage_realtime(operator_id, source='TripUpdates')

    veh_dfs = []
    # iterate through agency's AVL vehicles
    for entity in feed.entity:
        if entity.HasField('trip_update'):
            veh_id = entity.trip_update.vehicle.id
            stop_updates = [extract_stop_time_update(s) for s in entity.trip_update.stop_time_update]
            veh_df = pd.DataFrame(stop_updates)
            veh_df['vehicle_id'] = veh_id
            veh_dfs.append(veh_df)
    final_veh_df = pd.concat(veh_dfs, ignore_index=True)
    final_veh_df['agency_id'] = operator_id
    return final_veh_df


def pull_TripUpdates_real_time(to_csv=True):
    """Calls pull_agency_TripUpdates_real_time for each agency in
    OPERATOR_ID_MAP. Returns a dataframe of all real-time TripUpdates
    (including departure_time, stop_id) of AVL
    vehicles for each agency"""

    # initialize logger
    logger = init_logger('gtfs_real_time_TripUpdates_pull', OUTPUT_DIR)

    a = time.time()
    stop_dfs = []
    for operator in OPERATOR_ID_MAP.keys():
        try:
            agency_stops = pull_agency_TripUpdates_real_time(operator)
            stop_dfs.append(agency_stops)
        except Exception as e:
            # print('failed to pull TripUpdates for {}'.format(operator))
            # print(e)
            logger.info('failed to pull TripUpdates for {}'.format(operator))
            logger.info(e)
    final = pd.concat(stop_dfs, ignore_index=True)
    final['agency_name'] = final['agency_id'].map(OPERATOR_ID_MAP)
    b = time.time()
    logger.info('GTFS real time TripUpdates pull took {}'.format(print_runtime(b-a)))
    if to_csv:
        # write to output directory
        output_dir = os.path.join(OUTPUT_DIR, 'gtfs_real_time_pull')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_fname = os.path.join(output_dir, 'TripUpdates_real_time.csv')
        final.to_csv(output_fname, index=False)
        logger.info('output created at {}'.format(output_fname))
        # print('output created at {}'.format(output_fname))
    # if not writing to csv files, return the final DataFrame
    else:
        return final


def pull_511_gtfs_real_time():
    pull_VehiclePositions_real_time()
    pull_TripUpdates_real_time()


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
    #     operator_ids
    return operator_ids


if __name__ == '__main__':
    # operator_ids = get_operator_ids_from_511()
    # if not os.path.exists(OUTPUT_DIR):
    #     os.makedirs(OUTPUT_DIR)
    pull_511_gtfs_static(to_csv=False)
    # pull_511_gtfs_real_time()
   

