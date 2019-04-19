"""
This file contains GTFS feed transformations used for common GTFS tasks
(e.g. calculating headways, etc.)
"""

def get_eligible_SB50_agencies(calendar_df):
    """Given the calendar_all_agencies dataframe, returns a list of
    agencies which meet the Monday-Sunday service criteria for SB50.

    The original format of calendar.txt is separate lines for weekday,
    Saturday, and Sunday service. This function flattens the rows of the
    dataframe so that for each agency, all its service days are
    indicated as 1 in a single row. Then all agencies that offer
    Monday-Sunday (7 day) service are returned in a list.
    """
    # flatten service days for each agency
    service_day_cal = calendar.groupby(['agency_id'], as_index=False)[weekdays].max()
    # subset to agencies with 7 day service
    service_day_cal['days'] = service_day_cal[weekdays].sum(axis=1)
    service_day_cal = service_day_cal[service_day_cal['days'] == 7]
    SB50_agencies = list(service_day_cal['agency_id'])
    return SB50_agencies


def modify_trip_df(trips_df):
    """Given the trips_all_agencies dataframe, returns a modified table
    with renamed direction_id column values and a unique Route_Pattern_ID
    for each agency route (for headway calculations)"""
    modified_trips_df = trips_df.copy()
    route_pattern_id_cols = ['agency_id', 'route_id', 'direction_id']
    modified_trips_df[route_pattern_id_cols] = modified_trips_df[route_pattern_id_cols].astype(str)
    direction_id_map = {'0': 'Outbound', '1': 'Inbound'}
    modified_trips_df['direction_id'] = modified_trips_df['direction_id'].map(direction_id_map)
    modified_trips_df['Route_Pattern_ID'] = (modified_trips_df['agency_id']
                                    + '-' + modified_trips_df['route_id']
                                    + '-' + modified_trips_df['direction_id'])
    return modified_trips_df
