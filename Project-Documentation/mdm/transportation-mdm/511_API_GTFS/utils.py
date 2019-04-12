"""
This file contains commonly-used utility functions, such as logging, file I/O, etc.
"""

import os
import logging

def init_logger(logger_name, output_dir):
    """Given a logger_name and output_dir, sets the logging level to
    INFO and initializes logger to log to output_dir/<logger_name>.log
    and the console"""
    logger = logging.getLogger(logger_name)
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