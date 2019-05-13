import os
import sys
import pandas as pd
import ipywidgets as widgets

# local imports

from config import *
user = os.environ['USER']

sys.path.insert(0, '/Users/{}/Box/DataViz Projects/Utility Code'.format(user))
from utils_io import dump_json, makedirs_if_not_exists


def init_colmap_selector(column, options, default):
    colmap_dropdown = widgets.Dropdown(options=options,
                                     description='{}: '.format(column),
                                     value=default)

    SQL_input = widgets.Text(
                    placeholder='Type a SQL statement',
                    disabled=True,
                    description='SQL:')
    # Shows custom SQL text box
    def show_custom_SQL_input(change):
        """
        """
        if change['type'] == 'change' and change['name'] == 'value':
            if change['new'] == 'Enter your own SQL statement':
                SQL_input.disabled = False

    # Trigger show_custom_SQL_input if 'Type a SQL statement' is selected
    colmap_dropdown.observe(show_custom_SQL_input)
    return widgets.HBox([colmap_dropdown, SQL_input])


def display_colmap_menu(urbansim_table, county):
    """"""
    # allow user option of entering SQL statement
    options = ["'None'", 'Enter your own SQL statement'] + COUNTY_COLS[county]
    urbansim_cols = URBANSIM_COLS[urbansim_table]
    if urbansim_table == 'buildings':
        defaults = BUILDINGS_DEFAULTS[county]
    elif urbansim_table == 'parcels':
        defaults = PARCELS_DEFAULTS[county]

    urbansim_col_menus = {}
    for c in urbansim_cols:
        if c in defaults:
            default = defaults[c]
            col_options = set(options + [default])
        else:
            col_options = options
            default = col_options[0]
        urbansim_col_menus[c] = init_colmap_selector(c, col_options, default)
    # display dropdown menus
    for menu in urbansim_col_menus.values():
        display(menu)
    return urbansim_col_menus


def get_colmap_value(urbansim_col_menus, column):
    colmap_dropdown, SQL_input = urbansim_col_menus[column].children
    if colmap_dropdown.value == 'Enter your own SQL statement':
        colmap_value = SQL_input.value
    else:
        colmap_value = colmap_dropdown.value
    return colmap_value


def show_download_button(urbansim_col_menus, county, urbansim_table, output_fname=False):
    # output_fname = '~/Downloads/{}_colmap_{}.csv'.format(urbansim_table, county)
    if not output_fname:
        output_fname = '{}_colmap_{}'.format(urbansim_table, county)
    button = widgets.Button(description='Download')
    display(widgets.HBox([widgets.Label('Download column mapping: '), button]))

    def on_button_clicked(b):
        print('Downloading as {}'.format(output_fname))
        download_colmap(urbansim_col_menus, county, urbansim_table, output_fname)
        
    button.on_click(on_button_clicked)


def download_colmap(urbansim_col_menus, county, urbansim_table, output_fname):
    urbansim_cols = URBANSIM_COLS[urbansim_table]
    colmap_dict = {c: get_colmap_value(urbansim_col_menus, c) for c in urbansim_cols}
    colmap_df = pd.DataFrame.from_dict(colmap_dict, orient='index').reset_index()
    colmap_df.columns = ['MTC_urbansim_colname', 'County_colname']
    makedirs_if_not_exists(colmap_csv_output_dir)
    csv_output_fname = os.path.join(colmap_csv_output_dir, output_fname + '.csv')
    colmap_df.to_csv(csv_output_fname, index=False)
    makedirs_if_not_exists(colmap_json_output_dir)
    json_output_fname = os.path.join(colmap_json_output_dir, output_fname + '.json')
    dump_json(colmap_dict, json_output_fname)
