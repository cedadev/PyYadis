# -*- coding: utf-8 -*-

"""Top-level package for yadis_server."""

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.1.0"
from .app import YadisFlaskApp


def create_app():
    '''Convenience factory function for use with waitress e.g.
    
    `% waitress-serve --call 'yadis_server:app.create'`
    '''
    return YadisFlaskApp.create()