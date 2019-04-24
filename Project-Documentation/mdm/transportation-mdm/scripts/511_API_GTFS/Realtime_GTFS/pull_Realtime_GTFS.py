import os
import sys
import time
import pandas as pd
from urllib.request import urlopen
# Pre-requisite: ! pip install --upgrade gtfs-realtime-bindings
from google.transit import gtfs_realtime_pb2

import sys
sys.path.insert(0, '../')
from utils import (init_logger, print_runtime)
from GTFS_511_config import OUTPUT_DIR, OPERATOR_ID_MAP


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


if __name__ == '__main__':
    # set necessary variables
    DEV_511_API_KEY = os.environ['DEV_511_API_KEY']
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    pull_511_gtfs_real_time()
