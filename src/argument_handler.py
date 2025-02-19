#!/usr/bin/env python3

"""
Process user input
Python 3.13+
Date created: February 5th, 2025
Date modified: -
"""

import argparse
from argparse import Namespace


class ArgumentHandler:
    def __init__(self) -> None:
        """
        Initialization method
        """
        self.parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description="A tool for reading the browser's history file."
        )
        self._setup_arguments()

    def _setup_arguments(self):
        """
        Define all arguments here
        """
        self.parser.add_argument(
            "-w", "--websites", help="Show visited websites", action="store_true"
        )

        self.parser.add_argument(
            "-o", "--output", help="Create a text file", action="store_true"
        )

        self.parser.add_argument(
            "-v", "--version", help="Displays the current version", action="store_true"
        )

    def parse(self) -> Namespace:
        """
        Parse the command-line arguments

        Returns:
            _type_: The parsed arguments
        """
        return self.parser.parse_args()
