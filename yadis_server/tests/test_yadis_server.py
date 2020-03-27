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


_OPENID_URI_PATH_PREFIX = '/esgf-idp/openid/'

@pytest.fixture
def client():
    'Fixture for Yadis Flask App'
    test_config = {
        'OPENID_URI_PATH_PREFIX': _OPENID_URI_PATH_PREFIX,
        'ATTRIBUTE_SERVICE_URI': 'https://<host>/attribute-service/',
        'MYPROXY_SERVICE_URI': 'socket://<host>:7512',
        'SLCS_URI': 'https://<host>/onlineca/certificate/',
        'OAUTH_ACCESS_TOK_URI': 'https://<host>/oauth/access_token',
        'OAUTH_RESOURCE_URI': 'https://<host>/oauth/certificate/',
        'OAUTH_AUTHORIZE_URI': 'https://<host>/oauth/authorize'
        }
    app = YadisFlaskApp.create(config=test_config)
    testing_client = app.test_client()
    yield testing_client

   
def test_yadis_server(client):
    """Check GET generic XRDS response"""
    response = client.get(_OPENID_URI_PATH_PREFIX)
    
    assert response.status_code == 200
    assert b"<Service priority=" in response.data
   
def test_yadis_user(client):
    """Check GET user-specific XRDS response"""
    response = client.get(f'{_OPENID_URI_PATH_PREFIX}jbloggs')
    
    assert response.status_code == 200
    assert b"jbloggs</LocalID>" in response.data
      
