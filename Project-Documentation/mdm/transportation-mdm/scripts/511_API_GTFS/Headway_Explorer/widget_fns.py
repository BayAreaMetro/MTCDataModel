"""This file contains all widget functions for the Headway Explorer tool.

These functions are called in Headway_Explorer.ipynb (Headway Explorer tool)
"""

import os
import pandas as pd
import ipywidgets as widgets
from ipywidgets import HBox, VBox, Label


def init_day_type_button():
    """
    show_days_of_week derived from on_change code from https://stackoverflow.com/a/40165257
    """
    day_type_button = widgets.RadioButtons(
    options=['Weekday', 'Weekend', 'Select Day(s)'],
    description='Day type:'
    )

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_checkboxes = {}
    for d in weekdays:
        weekday_checkboxes[d] = widgets.Checkbox(value=False, description=d)

    # Shows days of week options
    def show_days_of_week(change):
        """If 'Select Day(s)' is selected from the Day type menu,
        shows a checkbox for each day of the week"""
        if change['type'] == 'change' and change['name'] == 'value':
            if change['new'] == 'Select Day(s)':
                for checkbox in weekday_checkboxes.values():
                    display(checkbox)
            else:
                for checkbox in weekday_checkboxes.values():
                    checkbox.disabled = True

    # Trigger show_days_of_week if 'Select Day(s)' is selected
    day_type_button.observe(show_days_of_week)
    return day_type_button, weekday_checkboxes


def get_days(day_type_button, weekday_checkboxes):
    """
    Returns a list of transit service days given a user's selection
    """
    weekdays = list(weekday_checkboxes.keys())
    if day_type_button.value == 'Weekday':
        days =  weekdays[:-2]
    elif day_type_button.value == 'Weekend':
        days =  weekdays[-2:]
    else:
        days = []
        for d in weekdays:
            if weekday_checkboxes[d].value:
                days.append(d)
    days = [d.lower() for d in days]
    print('you selected {}'.format(repr(days)))
    return days


def init_time_period_menu():
    """"""
    time_period_menu = widgets.Dropdown(
        options=['AM Peak (6-10AM)', 'PM Peak (3-7PM)',
                 'Standard weekday (6AM-10PM)',
                 'Standard weekend (8AM-10PM)',
                 'Enter your own'],
        description='Time period:'
        )
    
    def init_custom_time_selector():
        hours = widgets.Select(
            options=[str(i).zfill(2) for i in range(24)],
            description='hour:'
        )

        mins = widgets.Select(
            options=[str(i).zfill(2) for i in range(60)],
            description='minute:'
        )
        return hours, mins

    custom_time_dict = {'start': init_custom_time_selector(),
                        'end': init_custom_time_selector()}
    
    # Shows custom time options
    def set_custom_time(change):
        """If 'Enter your own' is selected from the Time period menu,
        shows a start and end time selector
        
        Widget layout code found here: https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Styling.html
        """
        if change['type'] == 'change' and change['name'] == 'value':
            if change['new'] == 'Enter your own':
                start_time_box = HBox([Label('Start time')] + list(custom_time_dict['start']))
                end_time_box = HBox([Label('End time')] + list(custom_time_dict['end']))
                display(VBox([start_time_box, end_time_box]))
                    
                    
    time_period_menu.observe(set_custom_time)
    return time_period_menu, custom_time_dict


def get_time_period(time_period_menu, custom_time_dict):
    if time_period_menu.value == 'AM Peak (6-10AM)':
        start_time = pd.Timedelta('06:00:00')
        end_time = pd.Timedelta('10:00:00')
    elif time_period_menu.value == 'PM Peak (3-7PM)':
        start_time = pd.Timedelta('15:00:00')
        end_time = pd.Timedelta('19:00:00')
    elif time_period_menu.value == 'Standard weekday (6AM-10PM)':
        start_time = pd.Timedelta('06:00:00')
        end_time = pd.Timedelta('22:00:00')
    elif time_period_menu.value == 'Standard weekend (8AM-10PM)':
        start_time = pd.Timedelta('08:00:00')
        end_time = pd.Timedelta('22:00:00')
    else:
        start_times = custom_time_dict['start']
        start_time = '{}:{}'.format(start_times[0].value, start_times[1].value)
        end_times = custom_time_dict['end']
        end_time = '{}:{}'.format(end_times[0].value, end_times[1].value)
        
        start_time = time_period_str_to_timedelta(start_time)
        end_time = time_period_str_to_timedelta(end_time)
        
        if start_time > end_time:
            print('The start time you entered is after the end time, switching them')

        if start_time == end_time:
            print('Start time and end time must be different')
            # currently can only access updated time_period_menu attributes after running display in cell above
#             time_period_menu, custom_time_dict = init_time_period_menu()
#             display(time_period_menu)
#             return get_time_period(time_period_menu, custom_time_dict)
    start_time_str = repr(start_time).split('days ')[1].strip("')")
    end_time_str = repr(end_time).split('days ')[1].strip("')")
    print('You selected start time of {} and end time of {}'.format(start_time_str, end_time_str))
    return start_time, end_time


def init_headway_selector():
    """
    """
    headway_selector = widgets.Dropdown(
                    options=['15 mins', '20 mins', '30 mins', 'Enter your own'],
                    description='Headway:'
                )

    custom_headway = widgets.FloatText(
        value=10,
        description='Headway:'
    )

    # Shows custom headway float entry box
    def show_custom_headway(change):
        """If 'Select Day(s)' is selected from the Day type menu,
        shows a checkbox for each day of the week"""
        if change['type'] == 'change' and change['name'] == 'value':
            if change['new'] == 'Enter your own':
                print('Enter your own max headways (float)')
                display(custom_headway)

    # Trigger show_custom_headway if 'Enter your own' is selected
    headway_selector.observe(show_custom_headway)
    return headway_selector, custom_headway


def get_headway(headway_selector, custom_headway):
    if headway_selector.value == '15 mins':
        headway = 15
    elif headway_selector.value == '20 mins':
        headway = 20
    elif headway_selector.value == '30 mins':
        headway = 30
    else:
        headway = custom_headway.value
    print('you selected a headway of {} mins'.format(headway))
    return headway


def show_download_button(df, calc_id):
    button = widgets.Button(description="Download Data")
    display(button)

    def on_button_clicked(b):
        print('Downloading as {}.csv'.format(calc_id))
        # : is changed to /, which ruins path
        output_fname = '~/Downloads/{}.csv'.format(calc_id).replace(':', '')
        # overwrite previously-downloaded file
        if os.path.isfile(output_fname):
            os.remove(output_fname)
        df.to_csv(output_fname, index=False)

    button.on_click(on_button_clicked)
