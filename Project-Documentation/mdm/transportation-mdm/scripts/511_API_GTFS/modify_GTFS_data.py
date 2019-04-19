"""
This file contains GTFS feed transformations used for common GTFS tasks
(e.g. calculating headways, etc.)

The functions in this file were derived from

https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/RouteBuilderStuff_KS.R
and

https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/r511.R

TODO: pull tables from Redshift, create interactive tool to allow users to specify time period and download resulting headways table

CURRENT PROMPT FOR TIME PERIOD INPUT:

print('Enter time using 24 hour HH:MM format, e.g. 22:10')

headway_start_time = input('Enter start time for headway calculation period: ')
headway_end_time = input('Enter end time for headway calculation period: ')

start_time_td = time_period_str_to_timedelta(headway_start_time)
end_time_td = time_period_str_to_timedelta(headway_end_time, start=False)

Run with:

python modify_GTFS_data.py
"""
import pandas as pd

# local import
from utils import time_period_str_to_timedelta, timedelta_to_time_period_str

def get_eligible_SB50_agencies(calendar_df):
    """
    Given the gtfs_calendar dataframe, returns a list of
    agencies which meet the Monday-Sunday service criteria for SB50.

    The original format of calendar.txt is separate lines for weekday,
    Saturday, and Sunday service. This function flattens the rows of the
    dataframe so that for each agency, all its service days are
    indicated as 1 in a single row. Then all agencies that offer
    Monday-Sunday (7 day) service are returned in a list.
    """
    weekdays = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    # flatten service days for each agency
    service_day_cal = calendar_df.groupby(['agency_id'], as_index=False)[weekdays].max()
    # subset to agencies with 7 day service
    service_day_cal['days'] = service_day_cal[weekdays].sum(axis=1)
    service_day_cal = service_day_cal[service_day_cal['days'] == 7]
    SB50_agencies = list(service_day_cal['agency_id'])
    return SB50_agencies


def modify_trip_df(trips_df):
    """
    Given the gtfs_trips dataframe, returns a modified table
    with renamed direction_id column values and a unique Route_Pattern_ID
    for each agency route (for headway calculations)
    """
    mod_trips_df = trips_df.copy()
    route_pattern_id_cols = ['agency_id', 'route_id', 'direction_id']
    mod_trips_df[route_pattern_id_cols] = mod_trips_df[route_pattern_id_cols].astype(str)
    direction_id_map = {'0': 'Outbound', '1': 'Inbound'}
    mod_trips_df['direction_id'] = mod_trips_df['direction_id'].map(direction_id_map)
    mod_trips_df['Route_Pattern_ID'] = (mod_trips_df['agency_id']
                                    + '-' + mod_trips_df['route_id']
                                    + '-' + mod_trips_df['direction_id'])
    return mod_trips_df


def modify_stop_times_df(stop_times_df):
    """
    Given the gtfs_stop_times dataframe, returns a modified table
    with corrected arrival time columns. In the original GTFS stop_times feed, the arrival
    time can exceed 24 hours since it goes by trips. For example, if a trip left at 11:50pm
    and arrived at 12:50am, the original arrival time would be 24:50, but the corrected arrival time would be 00:50
    """
    mod_stop_times_df = stop_times_df.copy()
    mod_stop_times_df['arrival_time_td'] = pd.to_timedelta(mod_stop_times_df['arrival_time'])
    overflow_times = mod_stop_times_df['arrival_time_td'] > pd.Timedelta('1 day')
    mod_stop_times_df.loc[overflow_times, 'arrival_time_td'] = (mod_stop_times_df.loc[overflow_times, 'arrival_time_td']
                                                                - pd.Timedelta('1 day'))
    return mod_stop_times_df


def subset_routes_df_buses(routes_df):
    """
    Given the gtfs_routes dataframe, returns a subsetted dataframe for only buses (route_type = 3)
    """
    return routes_df[routes_df['route_type'] == 3]


def calc_headways(trips_df, stop_times_df, routes_df, calendar_df, start_time_td, end_time_td):
    """
    Given pandas DataFrames gtfs_trips, gtfs_stop_times, gtfs_routes, and gtfs_calendar,
     and pandas Timedeltas start_time_td and end_time_td (which define the headway calculation period)
    calculates the headways for the specified time period
    """

    # add column Route_Pattern_ID
    mod_trips_df = modify_trip_df(trips_df)

    # subset routes to bus routes only
    bus_routes = subset_routes_df_buses(routes_df)
    
    # add column arrival_time_td
    mod_stop_times_df = modify_stop_times_df(stop_times_df)
    # subset stop_times to desired headway calculation time period
    subset_stop_times_df = mod_stop_times_df[mod_stop_times_df['arrival_time_td'].between(start_time_td, end_time_td)]
    
    routes_cols = ['route_id', 'route_type']
    trips_cols = ['agency_id', 'agency_name', 'route_id', 'direction_id',
                  'trip_headsign', 'trip_id', 'Route_Pattern_ID']
    stop_times_cols = ['trip_id', 'arrival_time_td', 'stop_id', 'stop_sequence']
    
    headways_table = (routes_df[routes_cols]
                      .merge(mod_trips_df[trips_cols])
                      .merge(subset_stop_times_df[stop_times_cols]))

    # subset table to eligible SB50 agencies (service Monday-Sunday)
    SB50_agencies = get_eligible_SB50_agencies(calendar_df)
    headways_table = headways_table[headways_table['agency_id'].isin(SB50_agencies)]
    
    # count number of times a trip stops at each stop in given time period
    headways_table['Total_Trips'] = (headways_table
                                        .groupby(['Route_Pattern_ID', 'trip_headsign', 'stop_id'])['stop_sequence']
                                        .transform('size'))
    # calculate the duration of the specified time frame
    time_frame_duration_mins = round((subset_df['arrival_time_td'].max()
                                       - subset_df['arrival_time_td'].min())
                                     .total_seconds() / 60.0)
    # calculate headway as time period duration/number of trips passing each stop
    headways_table['Headway'] = time_frame_duration_mins/headways_table['Total_Trips']

    headways_table['time_period'] = (timedelta_to_time_period_str(start_time_td)
                                     + '-'
                                     + timedelta_to_time_period_str(end_time_td))
    final_cols = ['agency_id', 'agency_name', 'route_id', 'direction_id',
                  'trip_headsign', 'Total_Trips', 'Headway', 'route_type',
                  'time_period', 'Route_Pattern_ID']
    headways_table = headways_table[final_cols]
    return headways_table


if __name__ == '__main__':
    pass
    # pull these tables from S3: trips_df, stop_times_df, routes_df, calendar_df
    # get user input to specify time period
    # output: download calculated headways table as csv


    