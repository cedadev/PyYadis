# -*- coding: utf-8 -*-

"""Yadis Flask app - simple module for running app.  Nb. this is best used for test only,
use waitress or other similar web application server for production
"""

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from .app import YadisFlaskApp


if __name__ == "__main__":
    YadisFlaskApp.create().run()