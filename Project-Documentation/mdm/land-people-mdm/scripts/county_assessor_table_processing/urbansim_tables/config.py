query_output_dir = 'redshift_cmds'
redshift_coltype_dir = 'redshift_column_types'
colmap_csv_output_dir = 'column_map_csvs'
colmap_json_output_dir = 'column_map_dicts'

parcels_2018_copy_cols = ['apn', 'joinid', 'jurisdict', 'fipco']

# Make into Redshift table?
fipco_mapping = {'Alameda': 'CA001',
                 'Contra Costa': 'CA013',
                 'Marin': 'CA041',
                 'Napa': 'CA055',
                 'San Francisco': 'CA075',
                 'San Mateo': 'CA081',
                 'Santa Clara': 'CA085',
                 'Solano': 'CA095',
                 'Sonoma': 'CA097'}


URBANSIM_COLS = {'buildings': ['apn',
                               'jurisdiction_cty',
                               'parcel_id',
                               'building_id',
                               'building_type',
                               'building_sqft',
                               'non_residential_sqft',
                               'residential_units',
                               'year_built',
                               'assessed_building_value',
                               'assessed_date',
                               'last_sale_price',
                               'last_sale_date',
                               'tenure',
                               'rent_type'],
                  'parcels': ['apn',
                              'jurisdiction_cty',
                              'parcel_id',
                              'assessed_land_value',
                              'assessed_date',
                              'acres',
                              'county_id',
                              'county',
                              'zone_id',
                              'taz22',
                              'maz',
                              'X',
                              'Y',
                              'juris_id',
                              'pda_id',
                              'tpa_id',
                              'opp_id',
                              'exp_id',
                              'exp_score',
                              'zoningmodcat']
                  }

COUNTY_COLS = {'Santa_Clara': ['addition_area',
                                   'addition_factor',
                                   'air_cond_flag',
                                   'apn',
                                   'assesseename1',
                                   'assesseename2',
                                   'audityrequip',
                                   'audityrpersonal',
                                   'basement_area',
                                   'basement_factor',
                                   'bath_rooms',
                                   'bedroom',
                                   'block_number',
                                   'building_num',
                                   'businvvalue',
                                   'cable_tv_flag',
                                   'cent_heat_flag',
                                   'citystate',
                                   'city_code',
                                   'condition_code',
                                   'const-class',
                                   'cov_parking',
                                   'datetransfer',
                                   'date_updated',
                                   'daytaxdefault',
                                   'dining_room',
                                   'dishwasher_flag',
                                   'docnumber',
                                   'docnumber2',
                                   'effective_year',
                                   'electric_flag',
                                   'elevator_flag',
                                   'exempttype',
                                   'expenses_percent',
                                   'extra_kitchen',
                                   'extra_plumb',
                                   'family_room',
                                   'fireplace_flag',
                                   'firstyrtaxdefaul',
                                   'first_floor_area',
                                   'fixedequipstruct',
                                   'garage-factor',
                                   'garage_area',
                                   'garage_conv_flag',
                                   'garage_port',
                                   'garbase-flag',
                                   'gas_flag',
                                   'gross_inc',
                                   'heat_air_cond',
                                   'hillside_flag',
                                   'homeownerexempt',
                                   'house_number',
                                   'house_suffix',
                                   'incareofname',
                                   'lake_stream_flag',
                                   'landvalue',
                                   'land_acres',
                                   'laundry_flag',
                                   'lease_area',
                                   'misc_costs',
                                   'model_num',
                                   'ms_class',
                                   'number_floors',
                                   'number_tenants',
                                   'number_units',
                                   'office_percent',
                                   'open_parking',
                                   'otherexemptions',
                                   'parcelflagasnona',
                                   'parcelflagpublic',
                                   'parking_ratio',
                                   'patio-code',
                                   'patio_bal_flag',
                                   'personalprop',
                                   'personalprop2',
                                   'pool_flag',
                                   'pool_sap_code',
                                   'porch_flag',
                                   'prevyrimproveval',
                                   'prevyrlandvalue',
                                   'property_type',
                                   'pub_code',
                                   'quality_class',
                                   'rec_room_flag',
                                   'remarks',
                                   'rentable_area',
                                   'sauna_flag',
                                   'school_code',
                                   'screen_room_flag',
                                   'second_flr_area',
                                   'securedimprove',
                                   'situs_seq_num',
                                   'special_prop-flg',
                                   'sprinklers_flag',
                                   'streetaddr',
                                   'street_direction',
                                   'street_name',
                                   'street_suffix',
                                   'taxratearea',
                                   'tax_rate_area',
                                   'tennis_flag',
                                   'third_floor_area',
                                   'totalexempt',
                                   'totalimprove',
                                   'total_area',
                                   'total_rooms',
                                   'tract_number',
                                   'traffic_zone',
                                   'unit_number',
                                   'unsecureflag',
                                   'usable_sq_feet',
                                   'usecode',
                                   'use_code',
                                   'utility_room',
                                   'vacancy_percent',
                                   'wall_height',
                                   'warehouse_pcnt',
                                   'water_flag',
                                   'wellflag',
                                   'xcorrobsolete',
                                   'ycorrobsolete',
                                   'year_built',
                                   'zip04',
                                   'zip05',
                                   'zip_code',
                                   'zip_code_ext',
                                   'zonecode',
                                   'zoning_code',
                                   'data_source',
                                   'building_id'],

                  }


BUILDINGS_DEFAULTS = {'Santa_Clara': {'apn': 'apn',
                                      'jurisdiction_cty': 'city_code',
                                      'building_type': 'use_code',
                                      'building_id': 'building_id',
                                      'building_sqft': 'total_area',
                                      'non_residential_sqft': 'usable_sq_feet - total_area',
                                      'residential_units': 'number_units',
                                      'year_built': 'year_built',
                                      'assessed_building_value': 'securedimprove',
                                      'assessed_date': 'date_updated',
                                      'last_sale_date': 'datetransfer',
                                      'tenure': "case when rentable_area/(total_area + 1)>= .5 then 'rent' else 'own' end"}
                                }

PARCELS_DEFAULTS = {'Santa_Clara': {'apn': 'apn',
                                     'jurisdiction_cty': 'city_code',
                                     'assessed_land_value': 'landvalue',
                                     'acres': 'land_acres',
                                     'assessed_date': 'date_updated',
                                     'juris_id': 'city_code',}
                                     }