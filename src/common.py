#!/usr/bin/env python3

"""
Common functions
Version: 1.0.0
Python 3.13+
Date created: February 7th, 2025
Date modified: -
"""

import logging
import platform
import sqlite3
import sys
from datetime import datetime as dt
from logging.config import fileConfig

# Add logger config
fileConfig("logging.ini")
logger = logging.getLogger()


def fetch_data(db, command):
    """
    Send queries to the sqlite database and return the result.
    :param db: The sqlite database
    :param command: The SQL command
    :return: The data from the sqlite database
    """
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(command)
        return cur.fetchall()
    except Exception as e:
        sys.exit(f"Error reading the database: {e}")


def system_info():
    """
    Check the running operating system.
    :return: Operating system name (and Windows version).
    """
    if platform.system() == "Darwin":
        return "macOS"
    elif platform.system() == "Linux":
        return "Linux"
    elif platform.system() == "Windows":
        version = platform.system() + " " + platform.release()
        return version


def convert_epoch(timestamp):
    """
    Convert epoch to human-readable date
    :param timestamp: The epoch timestamp.
    :return: The human-readable date.
    """
    try:
        rval = dt.fromtimestamp(timestamp / 1000000).ctime()
    except Exception as e:
        rval = "No date available (NULL value in database)."
        print(e)
    return rval
