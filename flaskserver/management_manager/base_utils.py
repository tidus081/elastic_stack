"""

BASE UTILS

Collection of utility functions for gRPC services in Prexcel project

Copyright 2018, Ikigai Labs.
All rights reserved.

"""
import logging
import sys
import logstash

def get_logger(name, level, logger_host="0.0.0.0", logger_port="5000"):
    """

    Get logger module

    Args:
        name (str): Name of the returning logger module
        level (str): Level of the logger module. ('info', 'error', or 'debug')

    Returns:
        (logging.logger): a logger module

    Raises:
        ValueError: If level arg not in ['info', 'error', 'debug']

    """
    if level == "info":
        logger_level = logging.INFO
    elif level == "error":
        logger_level = logging.ERROR
    elif level == "debug":
        logger_level = logging.DEBUG
    else:
        raise ValueError("Logger level should be 'info', 'error', or 'debug'")

    logging.basicConfig(level=logger_level,
                        format='%(asctime)s %(levelname)s-%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.StreamHandler(stream=sys.stdout),
                                  logstash.TCPLogstashHandler(logger_host, logger_port, version=1)])
    logger = logging.getLogger(name)

    return logger

