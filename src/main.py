#!/usr/bin/env python3

"""
Read data from Firefox browser and extract useful information.
OS: macOS only
Version: 1.0.0
Python 3.13+
Date created: February 4th, 2025
Date modified: February 7th, 2025
"""

import logging
from logging.config import fileConfig

from src import argument_handler
from src import firefox_data
from src import info

fileConfig("logging.ini")
logger = logging.getLogger()


def evaluate_args(args) -> None:
    """
    Evaluate the arguments passed by the user.

    Args:
        args (_type_): The arguments passed by the user.
    """

    if args.websites:
        logger.debug("Show visited websites")
        output: bool = args.output
        firefox_data.fetch_history_data(output)
    if args.version:
        logger.debug("Displays the current version")
        info.show_version()


def main() -> None:
    """
    Entry point of the program.
    """
    args_handler = argument_handler.ArgumentHandler()
    args = args_handler.parse()

    evaluate_args(args)


if __name__ == "__main__":
    main()
