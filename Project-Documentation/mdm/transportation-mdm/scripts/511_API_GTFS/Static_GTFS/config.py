from sqlalchemy import types

# specify desired files from each agency's GTFS feed
GTFS_FILES = ['agency.txt',
              'calendar.txt',
              'calendar_attributes.txt',
              'calendar_dates.txt',
              'directions.txt',
              'feed_info.txt',
              'routes.txt',
              # 'shapes.txt',  # not in feed for all agencies
              'stops.txt',
              'stop_times.txt',
              'trips.txt']

# for creating Redshift tables. Created manually after inspecting each GTFS feed file
gtfs_type_dict = {'gtfs_agency': {'agency_id': types.CHAR(2),
                                  'agency_name': types.VARCHAR(100),
                                  'agency_url': types.VARCHAR(100),
                                  'agency_timezone': types.VARCHAR(100),
                                  'agency_lang': types.VARCHAR(10),
                                  'agency_phone': types.VARCHAR(20),
                                  'agency_fare_url': types.VARCHAR(100),
                                  'agency_email': types.VARCHAR(100)
                                  },  # for agency.txt
                  'gtfs_calendar': {'service_id': types.CHAR(5),
                                     'monday': types.INTEGER,
                                     'tuesday': types.INTEGER,
                                     'wednesday': types.INTEGER,
                                     'thursday': types.INTEGER,
                                     'friday': types.INTEGER,
                                     'saturday': types.INTEGER,
                                     'sunday': types.INTEGER,
                                     'start_date': types.INTEGER,
                                     'end_date': types.INTEGER,
                                     'agency_id': types.CHAR(2),
                                     'agency_name': types.VARCHAR(100)
                                     },  # for calendar.txt
                  'gtfs_calendar_attributes': {'service_id': types.CHAR(5),
                                               'service_description': types.VARCHAR(100),
                                               'agency_id': types.CHAR(2),
                                               'agency_name': types.VARCHAR(100)
                                               },  # for calendar_attributes.txt
                  'gtfs_calendar_dates': {'service_id': types.CHAR(5),
                                         'date': types.INTEGER,
                                         'exception_type': types.INTEGER,
                                         'agency_id': types.CHAR(2),
                                         'agency_name': types.VARCHAR(100)
                                        },  # for calendar_dates.txt
                  'gtfs_directions': {'route_id': types.VARCHAR(20),
                                       'direction_id': types.INTEGER,
                                       'direction': types.VARCHAR(20),
                                       'agency_id': types.CHAR(2),
                                       'agency_name': types.VARCHAR(100)
                                      },  # for directions.txt
                  'gtfs_feed_info': {'feed_publisher_name': types.VARCHAR(100),
                                     'feed_publisher_url': types.VARCHAR(100),
                                     'feed_lang': types.VARCHAR(10),
                                     'feed_start_date': types.INTEGER,
                                     'feed_end_date': types.INTEGER,
                                     'feed_version': types.INTEGER,
                                     'agency_id': types.CHAR(2),
                                     'agency_name': types.VARCHAR(100)
                                    },  # for feed_info.txt
                  'gtfs_routes': {'route_id': types.VARCHAR(100),
                                 'agency_id': types.CHAR(2),
                                 'route_short_name': types.VARCHAR(100),
                                 'route_long_name': types.VARCHAR(100),
                                 'route_desc': types.VARCHAR(200),
                                 'route_type': types.INTEGER,
                                 'route_url': types.VARCHAR(200),
                                 'route_color': types.CHAR(6),
                                 'route_text_color': types.CHAR(6),
                                 'agency_name': types.VARCHAR(100)
                                },  # for routes.txt
                  'gtfs_stop_times': {'trip_id': types.VARCHAR(100),
                                     'arrival_time': types.VARCHAR(10),
                                     'departure_time': types.VARCHAR(10),
                                     'stop_id': types.VARCHAR(10),
                                     'stop_sequence': types.INTEGER,
                                     'stop_headsign': types.VARCHAR(100),
                                     'pickup_type': types.INTEGER,
                                     'drop_off_type': types.INTEGER,
                                     'shape_dist_traveled': types.FLOAT,
                                     'timepoint': types.INTEGER,
                                     'agency_id': types.CHAR(2),
                                     'agency_name': types.VARCHAR(100)
                                    },  # for stop_times.txt
                  'gtfs_stops': {'stop_id': types.VARCHAR(10),
                                 'stop_code': types.VARCHAR(10),
                                 'stop_name': types.VARCHAR(100),
                                 'stop_lat': types.FLOAT,
                                 'stop_lon': types.FLOAT,
                                 'zone_id': types.FLOAT,
                                 'stop_desc': types.VARCHAR(200),
                                 'stop_url': types.VARCHAR(100),
                                 'location_type': types.FLOAT,
                                 'parent_station': types.VARCHAR(20),
                                 'stop_timezone': types.VARCHAR(100),
                                 'wheelchair_boarding': types.FLOAT,
                                 'agency_id': types.CHAR(2),
                                 'agency_name': types.VARCHAR(100)
                                },  # for stops.txt
                  'gtfs_trips': {'route_id': types.VARCHAR(100),
                                 'service_id': types.VARCHAR(10),
                                 'trip_id': types.VARCHAR(100),
                                 'trip_headsign': types.VARCHAR(100),
                                 'direction_id': types.INTEGER,
                                 'block_id': types.VARCHAR(20),
                                 'shape_id': types.VARCHAR(50),
                                 'trip_short_name': types.VARCHAR(100),
                                 'bikes_allowed': types.FLOAT,
                                 'wheelchair_accessible': types.FLOAT,
                                 'agency_id': types.CHAR(2),
                                 'agency_name': types.VARCHAR(100)
                                }  # for trips.txt
                      }
