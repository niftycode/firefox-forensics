# firefox-forensics

![Static Badge](https://img.shields.io/badge/python-3.13-blue)
![GitHub License](https://img.shields.io/github/license/niftycode/firefox-forensics)
![](https://img.shields.io/github/issues/niftycode/firefox-forensics.svg?style=flat)
![](https://img.shields.io/pypi/v/firefox-forensics)
![GitHub last commit](https://img.shields.io/github/last-commit/niftycode/firefox-forensics)

This is a simple forensic tool written in Python. Use this tool to fetch the content (id, url, date of last visit) from the `places.sqlite` database file of the Firefox browser on macOS.

## Background

Firefox stores a variety of data in a directory called "Profiles." This directory also contains the `places.sqlite` database, which holds the browsing history. This program accesses that database and reads the `moz_places` table. It then displays three entries in the terminal: the ID, the visited website, and the date.

## Requirements

* Python 3.13 (It will probably work with other versions too, but I haven't tested it.)
* macOS

## Install

    pip3 install firefox-forensics

## Usage

To display the ID, the visited website and the date in the terminal, execute the following command:

    firefox-forensics -w

If this data should also be saved in a file on the desktop, the option `-o` must be added:

    firefox-forensics -w -o

## Changelog

see [Changelog.md](https://github.com/niftycode/firefox-forensics/blob/main/Changelog.md)
