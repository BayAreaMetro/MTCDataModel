"""
This file contains headway calulation functions for the Headway Explorer tool.

The functions in this file were derived from

https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/RouteBuilderStuff_KS.R
and
https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/r511.R


These functions are called in Headway_Explorer.ipynb (Headway Explorer tool)
"""
import sys
import pandas as pd

# local import
sys.path.insert(0, '../')
from utils import (time_period_str_to_timedelta,
 timedelta_to_time_period_str, pull_df_from_redshift_sql,
  create_redshift_engine)


def filter_calendar_days(df, subset_days):
    """Given a dataframe with weekday columns, filters the dataframe to rows
    that have service on the given subset days"""
    df['days'] = df[subset_days].sum(axis=1)
    filtered_df = df[df['days'] == len(subset_days)]
    return filtered_df


def modify_gtfs_calendar(gtfs_calendar):
    """The original format of calendar.txt is separate lines for weekday,
    Saturday, and Sunday service. This function flattens the rows of the
    dataframe so that for each agency, all its service days are
    indicated as 1 in a single row"""
    weekdays = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    # flatten service days for each agency
    mod_gtfs_calendar = gtfs_calendar.groupby(['agency_id'], as_index=False)[weekdays].max()
    return mod_gtfs_calendar


def modify_gtfs_trips(gtfs_trips):
    """
    Given the gtfs_trips dataframe, returns a modified table
    with renamed direction_id column values and a unique Route_Pattern_ID
    for each agency route (for headway calculations)
    """
    mod_gtfs_trips = gtfs_trips.copy()
    route_pattern_id_cols = ['agency_id', 'route_id', 'direction_id']
    mod_gtfs_trips[route_pattern_id_cols] = mod_gtfs_trips[route_pattern_id_cols].astype(str)
    direction_id_map = {'0': 'Outbound', '1': 'Inbound'}
    mod_gtfs_trips['direction_id'] = mod_gtfs_trips['direction_id'].map(direction_id_map)
    mod_gtfs_trips['Route_Pattern_ID'] = (mod_gtfs_trips['agency_id']
                                    + '-' + mod_gtfs_trips['route_id']
                                    + '-' + mod_gtfs_trips['direction_id'])
    return mod_gtfs_trips


def modify_gtfs_stop_times(gtfs_stop_times):
    """
    Given the gtfs_stop_times dataframe, returns a modified table
    with corrected arrival time columns. In the original GTFS stop_times feed, the arrival
    time can exceed 24 hours since it goes by trips. For example, if a trip left at 11:50pm
    and arrived at 12:50am, the original arrival time would be 24:50, but the corrected arrival time would be 00:50
    """
    mod_gtfs_stop_times = gtfs_stop_times.copy()
    mod_gtfs_stop_times['arrival_time_td'] = pd.to_timedelta(mod_gtfs_stop_times['arrival_time'])
    overflow_times = mod_gtfs_stop_times['arrival_time_td'] > pd.Timedelta('1 day')
    mod_gtfs_stop_times.loc[overflow_times, 'arrival_time_td'] = (mod_gtfs_stop_times.loc[overflow_times, 'arrival_time_td']
                                                                - pd.Timedelta('1 day'))
    return mod_gtfs_stop_times


def subset_gtfs_routes_buses(gtfs_routes):
    """
    Given the gtfs_routes dataframe, returns a subsetted dataframe for only buses (route_type = 3)
    """
    return gtfs_routes[gtfs_routes['route_type'] == 3]


def calc_headways(gtfs_trips, gtfs_stop_times, gtfs_routes, gtfs_calendar, max_headway, service_days, time_period):
    """
    Given pandas DataFrames gtfs_trips, gtfs_stop_times, gtfs_routes, and gtfs_calendar,
     and pandas Timedeltas start_time_td and end_time_td (which define the headway calculation period)
    calculates the headways for the specified time period
    """
    # add column Route_Pattern_ID
    mod_gtfs_trips = modify_gtfs_trips(gtfs_trips)
    # flatten service days
    mod_gtfs_calendar = modify_gtfs_calendar(gtfs_calendar)

    merged_trips = mod_gtfs_trips.merge(mod_gtfs_calendar)
    filtered_trips = filter_calendar_days(merged_trips, service_days)

    # subset routes to bus routes only
    bus_routes = subset_gtfs_routes_buses(gtfs_routes)
    
    # add column arrival_time_td
    mod_gtfs_stop_times = modify_gtfs_stop_times(gtfs_stop_times)
    # subset stop_times to desired headway calculation time period
    subset_gtfs_stop_times = mod_gtfs_stop_times[mod_gtfs_stop_times['arrival_time_td'].between(time_period['start_time_td'],
                                                                                          time_period['end_time_td'])]
    
    routes_cols = ['route_id', 'route_type']
    trips_cols = ['agency_id', 'agency_name', 'route_id', 'direction_id',
                  'trip_headsign', 'trip_id', 'Route_Pattern_ID']
    stop_times_cols = ['trip_id', 'arrival_time_td', 'stop_id', 'stop_sequence']
    
    headways_table = (bus_routes[routes_cols]
                      .merge(filtered_trips[trips_cols])
                      .merge(subset_gtfs_stop_times[stop_times_cols]))

    # subset table to desired service days
    filtered_calendar_df = filter_calendar_days(mod_gtfs_calendar, service_days)
    SB50_agencies = list(filtered_calendar_df['agency_id'])

    headways_table = headways_table[headways_table['agency_id'].isin(SB50_agencies)]
    
    # drop duplicate observations for the same stop at the same time period.
    dedup_cols = ['Route_Pattern_ID', 'trip_headsign', 'stop_id', 'stop_sequence',
                  'arrival_time_td', 'route_type']
    headways_table.drop_duplicates(subset=dedup_cols, inplace=True)
    
    # count number of times a trip stops at each stop in given time period
    headways_table['Total_Trips'] = (headways_table
                                        .groupby(['Route_Pattern_ID', 'trip_headsign', 'stop_id'])['stop_sequence']
                                        .transform('size'))
    # calculate the duration of the specified time frame
    time_frame_duration_mins = round((headways_table['arrival_time_td'].max()
                                       - headways_table['arrival_time_td'].min())
                                     .total_seconds() / 60.0)
    # calculate headway as time period duration/number of trips passing each stop
    headways_table['Headway'] = time_frame_duration_mins/headways_table['Total_Trips']
    
    # get average headway and number of trips by (agency, route id, route direction, trip)
    headways_table[['Avg_Headway', 'Avg_Num_Trips']] = (headways_table
                                                         .groupby(['Route_Pattern_ID', 'trip_headsign'])[['Headway', 'Total_Trips']]
                                                         .transform('mean'))
    
    # subset table to specified headways
    headways_table = headways_table[headways_table['Avg_Headway'] <= max_headway]
    

    headways_table['time_period'] = (timedelta_to_time_period_str(time_period['start_time_td'])
                                     + '-'
                                     + timedelta_to_time_period_str(time_period['end_time_td']))
    # final columns
    final_cols = ['agency_id', 'agency_name', 'route_id', 'direction_id',
                  'trip_headsign', 'Total_Trips', 'Headway', 'Avg_Headway', 'Avg_Num_Trips',
                  'route_type', 'time_period', 'Route_Pattern_ID']
    headways_table = headways_table[final_cols]
    return headways_table


def pull_GTFS_tables():
    """Pulls the necessary GTFS tables (gtfs_trips, GTFS_stop_times,
    GTFS_routes, GTFS_calendar) from Redshift and returns them as
    a dictionary of pandas DataFrames"""
    df_dict = {}
    GTFS_tables = ['gtfs_trips', 'gtfs_stop_times',
                   'gtfs_routes', 'gtfs_calendar']
    for tablename in GTFS_tables:
        sql_q = 'SELECT * FROM transportation.{};'.format(tablename)
        df_dict[tablename] = pull_df_from_redshift_sql(sql_q)
    return df_dict


if __name__ == '__main__':
    SB50_defs = {'1A': {'max_headway': 15,
                    'service_day_type': 'Weekday',
                    'time_period': {'start_time_td': pd.Timedelta('06:00:00'),
                                     'end_time_td': pd.Timedelta('10:00:00')}
                  },  # max 15 min headways during weekday peaks (M-F, 6-10 AM, 3-7 PM)
                 '1B': {'max_headway': 15,
                        'service_day_type': 'Weekday',
                        'time_period': {'start_time_td': pd.Timedelta('15:00:00'),
                                        'end_time_td': pd.Timedelta('19:00:00')}
                      },  # max 15 min headways during weekday peaks (M-F, 6-10 AM, 3-7 PM)
                 '2': {'max_headway': 20,
                       'service_day_type': 'Weekday',
                       'time_period': {'start_time_td': pd.Timedelta('06:00:00'),
                                        'end_time_td': pd.Timedelta('22:00:00')}
                      },  # max 20 min headways during weekdays (M-F, 6AM-10PM)
                 '3': {'max_headway': 30,
                       'service_day_type': 'Weekend',
                       'time_period': {'start_time_td': pd.Timedelta('08:00:00'),
                                        'end_time_td': pd.Timedelta('22:00:00')}
                      }  # max 30 min headways during weekends (Sat-Sun, 8AM-10PM)
                    }
