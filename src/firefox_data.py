#!/usr/bin/env python3

"""
Firefox data extraction
Python 3.13+
Date created: February 7th, 2025
Date modified: February 18th, 2025
"""

import getpass
import logging
import os
import sys
from logging.config import fileConfig

from src import common

fileConfig("logging.ini")
logger = logging.getLogger()


def fetch_history_data(save: bool) -> None:
    """
    Check the current operating system.
    Invoke the functions that check the database path,
    read the database file and print the data.

    Args:
        save (bool): Save the output to a file.
    """

    logger.debug(f"Output: {save}")

    os_version = common.system_info()
    history_file = "places.sqlite"
    db = firefox_db_path(os_version, history_file)
    print()
    print("The path to the database is: {}".format(db))
    print()

    history_data = read_history(db)

    print()
    print("Show the id, the URL and the last date:")
    print("=======================================")
    print()

    desktop_path = "/Users/{0}/Desktop/".format(getpass.getuser())

    if save:
        with open(desktop_path + "history_data.txt", "w") as file:
            for line in history_data:
                (
                    id,
                    url,
                    title,
                    rev_host,
                    visit_count,
                    hidden,
                    typed,
                    frequency,
                    last_visit_date,
                    guid,
                    foreign_count,
                    url_hash,
                    description,
                    preview_image_url,
                    site_name,
                    origin_id,
                    recalc_frequency,
                    alt_frequency,
                    recalc_alt_frequency,
                ) = line

                date = common.convert_epoch(last_visit_date)

                output = f"id: {str(id)}\nURL: {url}\nDate of last visit: {str(date)}\n"
                print(output)
                file.write(output + "\n")
    else:
        for line in history_data:
            (
                id,
                url,
                title,
                rev_host,
                visit_count,
                hidden,
                typed,
                frequency,
                last_visit_date,
                guid,
                foreign_count,
                url_hash,
                description,
                preview_image_url,
                site_name,
                origin_id,
                recalc_frequency,
                alt_frequency,
                recalc_alt_frequency,
            ) = line

            date = common.convert_epoch(last_visit_date)

            output = f"id: {str(id)}\nURL: {url}\nDate of last visit: {str(date)}\n"
            print(output)
        print("No output file created.")


def platform_paths():
    """
    Get the path to the Firefox profiles directory.

    Returns:
        str: The path to the Firefox profiles directory.
    """
    paths = {
        "Windows 7": "C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles".format(
            getpass.getuser()
        ),
        "Windows 8": "C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles".format(
            getpass.getuser()
        ),
        "Windows 10": "C:\\Users\\{0}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles".format(
            getpass.getuser()
        ),
        "Linux": "/home/{0}/.mozilla/firefox/".format(getpass.getuser()),
        "Darwin": "/Users/{0}/Library/Application Support/Firefox/Profiles".format(
            getpass.getuser()
        ),
    }

    return paths


def profile_paths(operating_system):
    """
    Check the current operating system.

    Args:
        operating_system (str): The current operating system.

    Returns:
        str: The path to the Firefox profiles directory.
    """

    profile_path = ""
    platform_path = platform_paths()

    # Check the operating system
    if operating_system == "Windows 7":
        print("Sorry, Windows 7 is not supported!")
    elif operating_system == "Windows 8":
        print("Sorry, Windows 8 is not supported!")
    elif operating_system == "Windows 10":
        print("Sorry, Windows 10 is not supported!")
    elif operating_system == "Linux":
        print("Sorry, Linux is not supported!")
    elif operating_system == "macOS":
        profile_path = platform_path["Darwin"]
    else:
        print("Error: Unknown Operating System!")
    return profile_path


def firefox_db_path(operating_system, db_file):
    """
    Check the path to the history database file.

    Args:
        operating_system (str): The current operating system.
        db_file (str): The name of the database file.

    Returns:
        _type_: The full path to the database.
    """

    profile_path = profile_paths(operating_system)

    # Try to find the x.default directory in Profiles folder.
    try:
        for item in os.listdir(profile_path):
            # Check for the x.default directory
            # and return the database file's path
            if os.path.isdir(os.path.join(profile_path, item)) and "release" in item:
                if os.path.isfile(os.path.join(profile_path, item, db_file)):
                    return os.path.join(profile_path, item, db_file)
    except FileNotFoundError as e:
        print(e)
        sys.exit(
            "Could not find Firefox Profiles folder!\nAre you sure Firefox is installed on this system?"
        )


def read_history(history_db):
    """
    Read the history database file (places.sqlite)

    Args:
        history_db (str): The name of the database file.

    Returns:
        str: The data from the history database.
    """

    sql_command = "SELECT * FROM moz_places"
    rval = common.fetch_data(history_db, sql_command)
    return rval
