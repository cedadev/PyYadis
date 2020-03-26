#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `yadis_server` package."""

__author__ = """Philip Kershaw"""
__contact__ = 'philip.kershaw@stfc.ac.uk'
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
import unittest
import os
import tempfile
import pytest

from ..app import YadisFlaskApp


@pytest.fixture
def client():
    'Fixture for Yadis Flask App'
    app = YadisFlaskApp.create()
    testing_client = app.test_client()
    yield testing_client

   
def test_yadis_server(client):
    """Check GET generic XRDS response"""
    response = client.get('/openid/')
    
    assert response.status_code == 200
    assert b"<Service priority=" in response.data
   
def test_yadis_user(client):
    """Check GET user-specific XRDS response"""
    response = client.get('/openid/jbloggs')
    
    assert response.status_code == 200
    assert b"jbloggs</LocalID>" in response.data
      
