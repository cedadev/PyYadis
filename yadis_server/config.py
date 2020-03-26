# -*- coding: utf-8 -*-

"""Yadis Flask app config settings."""

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
# Path prefix for OpenID URIs.  ESGF stock implementation uses
OPENID_URI_PATH_PREFIX = '/esgf-idp/openid/'

# CEDA implementation uses this prefix
#OPENID_URI_PATH_PREFIX = '/openid/'

# Sample settings for CEDA's XRDS
ATTRIBUTE_SERVICE_URI = 'https://sandstorm.ceda.ac.uk/attribute-service/'
MYPROXY_SERVICE_URI = 'socket://slcs1.ceda.ac.uk:7512'
SLCS_URI = 'https://slcs.ceda.ac.uk/onlineca/certificate/'
OAUTH_ACCESS_TOK_URI = 'https://slcs.ceda.ac.uk/oauth/access_token'
OAUTH_RESOURCE_URI = 'https://slcs.ceda.ac.uk/oauth/certificate/'
OAUTH_AUTHORIZE_URI = 'https://slcs.ceda.ac.uk/oauth/authorize'
