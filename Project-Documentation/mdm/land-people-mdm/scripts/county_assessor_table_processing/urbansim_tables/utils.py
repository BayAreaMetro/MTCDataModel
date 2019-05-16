"""
This file contains utility functions for BASIS data processing (I/O, etc.)
"""

import io
import os
import sys
import glob
import json
import pandas as pd

from config import query_output_dir, parcels_2018_copy_cols

user = os.environ['USER']

sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Utility Code'.format(user))
from utils_io import *


def create_urbansim_table(tablename, column_type_dict):
    """
    Creates Urbansim tables: buildings, parcels, planned land use
    """
    drop_table_s = 'DROP TABLE IF EXISTS {}'.format(tablename)
    table_s = create_redshift_table_str(tablename,
                                        column_type_dict=column_type_dict)
    # add apn as the DISTKEY and SORTKEY
    table_s = table_s.strip(';') + ' DISTKEY(apn) SORTKEY(apn);'

    copy_cols = ', '.join(parcels_2018_copy_cols)

    insert_into_s = """INSERT INTO {} ({})
    (SELECT {}
     FROM basis.parcels_2018);""".format(tablename, copy_cols, copy_cols)
    

    cmds = [drop_table_s, table_s, insert_into_s]

    # execute queries
    execute_redshift_cmds(cmds)

    # write queries
    makedirs_if_not_exists(query_output_dir)
    sql_output_fname = os.path.join(query_output_dir, 'create_{}.sql'.format(tablename))
    write_sql_cmds(cmds, sql_output_fname)


def create_select_with_rename_str(tablename, rename_d, distinct=True):
    colmapping_str = ''
    for k, v in rename_d.items():
        mapping = '{} as {},\n'.format(v, k)
        colmapping_str += mapping
    colmapping_str = colmapping_str.strip(',\n')
    if distinct:
        select_s = 'SELECT DISTINCT {} FROM {}'.format(colmapping_str, tablename)
    else:
        select_s = 'SELECT {} FROM {}'.format(colmapping_str, tablename)
    return select_s


def update_urbansim_table_county(tablename, county_table, staging_table, colmapping):
    """
    Follows procedure at http://www.silota.com/blog/amazon-redshift-upsert-support-staging-table-replace-rows/  # noqa
    
    Steps: 

    - start with basis.urbansim_buildings having [apn, joinid, jurisdict
         as jurisdiction, fipco] populated from basis.parcels_2018
    - create staging table basis.buildings_stage with identical schema
         to basis.urbansim_buildings and all columns up to date
        - copy basis.santa_clara_county_characteristics columns with
         rename (also compute missing columns) to basis.buildings_stage
        - match key cols from basis.parcels_2018 by APN
    - delete rows in basis.urbansim_buildings that correspond to
     basis.buildings_stage
    - insert basis.buildings_stage into basis.urbansim_buildings
    - drop basis.buildings_stage
    """

    drop_table_s = 'DROP TABLE IF EXISTS {};'.format(staging_table)

    select_str = create_select_with_rename_str(county_table, colmapping, distinct=True)


    create_staging_s = """CREATE TABLE {} AS 
    SELECT * FROM
    ({}) AS stage
    LEFT JOIN
    (SELECT apn, joinid, jurisdict, fipco
     FROM basis.parcels_2018) AS parcels
    USING(apn);""".format(staging_table, select_str)

    delete_from_s = """DELETE FROM {}
                      USING {}
                      WHERE {}.apn = {}.apn;""".format(tablename, staging_table,
                                                       tablename, staging_table)

    update_cols = [c for c in colmapping if colmapping[c] != "'None'"]
    update_cols = ', '.join(set(update_cols + parcels_2018_copy_cols))
    insert_into_s = """INSERT INTO {}({})
                       (SELECT {} FROM {});""".format(tablename, update_cols,
                                                      update_cols, staging_table)
    
    cmds = [drop_table_s, create_staging_s,
            delete_from_s, insert_into_s, drop_table_s]
    # execute queries
    execute_redshift_cmds(cmds)
    sql_output_fname = os.path.join(query_output_dir, 'update_{}_from_{}.sql'.format(tablename, county_table))
    write_sql_cmds(cmds, sql_output_fname)
