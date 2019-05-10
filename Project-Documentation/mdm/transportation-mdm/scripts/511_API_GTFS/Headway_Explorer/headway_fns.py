"""
This file contains headway calulation functions for the Headway Explorer tool.

The functions in this file were derived from

https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/RouteBuilderStuff_KS.R
and
https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/R/r511.R


These functions are called in Headway_Explorer.ipynb (Headway Explorer tool)
"""
import sys
import numpy as np
import pandas as pd

# local import
sys.path.insert(0, '../')
from utils import (time_period_str_to_timedelta,
 timedelta_to_hour_str, pull_df_from_redshift_sql,
  create_redshift_engine)


def filter_calendar_days(df, subset_days):
    """Given a dataframe with weekday columns, filters the dataframe to rows
    that have service on the given subset days"""
    df['days'] = df[subset_days].sum(axis=1)
    filtered_df = df[df['days'] == len(subset_days)]
    return filtered_df


def modify_gtfs_stops(gtfs_stops):
    """
    """
    mod_gtfs_stops = gtfs_stops.copy()
    gtfs_stops_cols = ['stop_id', 'stop_lat', 'stop_lon', 'agency_id', 'agency_name']
    return mod_gtfs_stops[gtfs_stops_cols]


def modify_gtfs_calendar(gtfs_calendar, flatten=False):
    """The original format of calendar.txt is separate lines for weekday,
    Saturday, and Sunday service. This function flattens the rows of the
    dataframe so that for each agency, all its service days are
    indicated as 1 in a single row"""
    mod_gtfs_calendar = gtfs_calendar.copy()
    weekdays = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
    # flatten service days for each agency
    if flatten:
        mod_gtfs_calendar = mod_gtfs_calendar.groupby(['agency_id'], as_index=False)[weekdays].max()
    gtfs_calendar_cols = weekdays + ['service_id', 'agency_id', 'agency_name']
    return mod_gtfs_calendar[gtfs_calendar_cols]


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
    gtfs_trips_cols = ['route_id', 'service_id', 'trip_id',
                       'trip_headsign', 'direction_id', 'agency_id',
                       'agency_name', 'Route_Pattern_ID']
    return mod_gtfs_trips[gtfs_trips_cols]


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
    gtfs_stop_times_cols = ['trip_id', 'arrival_time', 'arrival_time_td',
                            'stop_id', 'stop_sequence', 'agency_id', 'agency_name']
    return mod_gtfs_stop_times[gtfs_stop_times_cols]


def modify_gtfs_routes(gtfs_routes, route_type=None):
    """
    Given the gtfs_routes dataframe, returns a subsetted dataframe for only buses (route_type = 3)
    """
    mod_gtfs_routes = gtfs_routes.copy()
    if route_type is not None:
        mod_gtfs_routes = mod_gtfs_routes[mod_gtfs_routes['route_type'] == route_type]

    gtfs_routes_cols = ['route_id', 'route_type', 'agency_id', 'agency_name']
    return mod_gtfs_routes[gtfs_routes_cols]


def modify_trips_stop_times(mod_trips, mod_stop_times):
    df = mod_trips.merge(mod_stop_times)

    df['Route_Start_Time'] = df.groupby('route_id')['arrival_time_td'].transform(min)
    df['Route_Stop_Time'] = df.groupby('route_id')['arrival_time_td'].transform(max)

    def get_hour(x):
        return x.components.hours
    
    df['Route_Start_Hour'] = df['Route_Start_Time'].map(get_hour)
    df['Route_Stop_Hour'] = df['Route_Stop_Time'].map(get_hour)
    
    agency_route_stop_id_cols = ['agency_id', 'route_id', 'stop_id']
    df[agency_route_stop_id_cols] = df[agency_route_stop_id_cols].astype(str)
    df['Agency_Route_Stop_ID'] = (df['agency_id']
                                        + '-' + df['route_id']
                                        + '-' + df['stop_id'])
    return df


def pull_GTFS_tables():
    """Pulls the necessary GTFS tables (gtfs_trips, gtfs_stop_times,
    gtfs_routes, gtfs_calendar) from Redshift and returns them as
    a dictionary of pandas DataFrames"""
    df_dict = {}
    GTFS_tables = ['gtfs_trips', 'gtfs_stop_times',
                   'gtfs_routes', 'gtfs_calendar',
                   'gtfs_stops']
    for tablename in GTFS_tables:
        sql_q = 'SELECT * FROM transportation.{};'.format(tablename)
        df_dict[tablename] = pull_df_from_redshift_sql(sql_q)
    return df_dict


def compute_route_pattern_schedule(df_d):
    # get RoutePatternID
    mod_trips = modify_gtfs_trips(df_d['gtfs_trips'])

    # create arrival_time_td column
    mod_stop_times = modify_gtfs_stop_times(df_d['gtfs_stop_times'])

    mod_calendar = modify_gtfs_calendar(df_d['gtfs_calendar'])
    mod_routes = modify_gtfs_routes(df_d['gtfs_routes'])
    mod_stops = modify_gtfs_stops(df_d['gtfs_stops'])
    # merge data
    t_st = modify_trips_stop_times(mod_trips, mod_stop_times)
    t_st_c = t_st.merge(mod_calendar)
    t_st_c_s = t_st_c.merge(mod_stops)
    final_df = t_st_c_s.merge(mod_routes)
    return final_df


def create_route_pattern_schedule():
    df_d = pull_GTFS_tables()
    df = compute_route_pattern_schedule(df_d)
    s3_bucket = 'mtc-basis'
    s3_key = 'transportation/511_GTFS/Route_Pattern_Schedule.csv'
    post_df_to_s3(final_df, s3_bucket, s3_key)

    ctype_d = create_redshift_column_type_dict(df)
    s3_path = 's3://{}/{}'.format(s3_bucket, s3_key)
    tablename = 'transportation.route_pattern_schedule'
    create_redshift_table_via_s3(tablename, s3_path, column_type_dict=ctype_d)


def get_headway_calc_period_str(service_days, start_time_td, end_time_td):
    """Creates a string that defines the headway calculation period.

    This string is used to store headway calculations for that given time period
    """
    day_abbrev_d = {'monday': 'M',
                    'tuesday': 'T',
                    'wednesday': 'W',
                    'thursday': 'R',
                    'friday': 'F',
                    'saturday': 'Sat',
                    'sunday': 'Sun'}
    weekdays = list(day_abbrev_d.keys())[:-2]
    weekends = list(day_abbrev_d.keys())[-2:]
    if service_days == weekdays:
        headway_calc_days = 'Weekday'
    elif service_days == weekends:
        headway_calc_days = 'Weekend'
    else:
        headway_calc_days = ''.join([day_abbrev_d[d] for d in service_days])

    if start_time_td == pd.Timedelta('0 days 06:00:00') and end_time_td == pd.Timedelta('0 days 10:00:00'):
        time_period = 'AM_Peak'
    elif start_time_td == pd.Timedelta('0 days 15:00:00') and end_time_td == pd.Timedelta('0 days 19:00:00'):
        time_period = 'PM_Peak'
    else:
        # format '06:00-10:00'
        time_period = timedelta_to_hour_str(start_time_td)+ '-' + timedelta_to_hour_str(end_time_td)

    headway_calc_period_str = headway_calc_days + '_' + time_period
    return headway_calc_period_str


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
    
    headway_calc_period_str = get_headway_calc_period_str(service_days,
                                                          time_period['start_time_td'],
                                                          time_period['end_time_td'])
    # compute average headway and trip counts for the calculation time period
    # (by agency, route id, route direction, trip)
    headways_col = headway_calc_period_str + '_Headway'
    num_trips_col = headway_calc_period_str + '_Num_Trips'
    compute_cols = [headways_col, num_trips_col]

    headways_table[compute_cols] = (headways_table
        .groupby(['Route_Pattern_ID', 'trip_headsign'])[['Headway', 'Total_Trips']]
        .transform('mean'))

    # flag whether route meets specified headway criteria
    rows_meet_criteria = headways_table[headways_col] <= max_headway
    headways_table['Meets_criteria'] = np.where(rows_meet_criteria, 1, 0)
    
    headways_table['time_period'] = (timedelta_to_hour_str(time_period['start_time_td'])
                                     + '-'
                                     + timedelta_to_hour_str(time_period['end_time_td']))
    
    # final columns
    final_cols = (['agency_id', 'agency_name', 'route_id', 'direction_id',
                   'trip_headsign', 'route_type',  'Route_Pattern_ID']
                    + compute_cols
                    + ['time_period', 'Meets_criteria'])
    headways_table = headways_table[final_cols]

    # round final output to nearest int
    headways_table = headways_table.round(0)
    headways_table[compute_cols] = headways_table[compute_cols].astype(int)

    headways_table.drop_duplicates(inplace=True)
    return headways_table


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
