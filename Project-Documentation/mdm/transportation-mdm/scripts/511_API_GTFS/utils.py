"""
This file contains utility functions for Transit Data Processing,
such as logging, file I/O, moving data to AWS, etc.
"""

import os
import sys
import logging
# Pre-requisite: ! conda install -y -c anaconda psycopg2
import psycopg2
# Pre-requisite: ! pip install sqlalchemy-redshift
from sqlalchemy import create_engine

# local imports
sys.path.insert(0, '/Users/ktollas/licenses')
from credentials import REDSHIFT_USERNAME, REDSHIFT_PSWD


def init_logger(logger_name, output_dir):
    """Given a logger_name and output_dir, sets the logging level to
    INFO and initializes logger to log to output_dir/<logger_name>.log
    and the console"""
    logger = logging.getLogger(logger_name)
    # otherwise this step fails
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    log_fname = os.path.join(output_dir, '{}.log'.format(logger_name))
    fileHandler = logging.FileHandler(log_fname)
    logger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    logger.addHandler(consoleHandler)
    logger.setLevel(logging.INFO)
    return logger


def print_runtime(run_seconds):
    """Given a float of runtime seconds, formats the time for more readable logging"""
    if run_seconds > 60:
        mins = run_seconds/60.0
        if mins < 60:
            return '{} minutes'.format(round(mins, 4))
        else:
            return '{} hours'.format(round(mins/60.0, 4))
    else:
        return '{} seconds'.format(round(run_seconds, 4))


def post_df_as_redshift_table(tablename, df, dtypes=None):
    """Given a tablename, pandas DataFrame, and optionally a dictionary
    of table columns to sqlalchemy dtypes, writes the DataFrame as a Redshift table

    Resource: http://measureallthethin.gs/blog/connect-python-and-pandas-to-redshift/
    """
    redshift_connection_params = {'user': REDSHIFT_USERNAME,
                                  'password': REDSHIFT_PSWD,
                                  'port': 5439,
                                  'host': 'data-viz-cluster.cepkffrgvgkl.us-west-2.redshift.amazonaws.com',
                                  'dbname': 'dev'}

    psql_engine_str = 'redshift+psycopg2://{}:{}@{}:{}/{}'.format(redshift_connection_params['user'],
                                                             redshift_connection_params['password'],
                                                             redshift_connection_params['host'],
                                                             redshift_connection_params['port'],
                                                            redshift_connection_params['dbname'])

    engine = create_engine(psql_engine_str, echo=True)
    to_Redshift_args = {'name': tablename,
                        'schema': 'transportation',
                        'con': engine,
                        'index': False,
                        'if_exists': 'replace'}
    if dtypes is not None:
        to_Redshift_args['dtype'] = dtypes
    df.to_sql(**to_Redshift_args)
