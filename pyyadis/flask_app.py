# -*- coding: utf-8 -*-

"""Main module."""

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from flask import Flask, escape, request
from markupsafe import escape

app = Flask(__name__)


ATTRIBUTE_SERVICE_URI = 'https://sandstorm.ceda.ac.uk/attribute-service/'
MYPROXY_SERVICE_URI = 'socket://slcs1.ceda.ac.uk:7512'
SLCS_URI = 'https://slcs.ceda.ac.uk/onlineca/certificate/'
OAUTH_ACCESS_TOK_URI = 'https://slcs.ceda.ac.uk/oauth/access_token'
OAUTH_RESOURCE_URI = 'https://slcs.ceda.ac.uk/oauth/certificate/'
OAUTH_AUTHORIZE_URI = 'https://slcs.ceda.ac.uk/oauth/authorize'

@app.route('/openid/<username>')
def yadis_personal_response(username):
    '''Respond to Yadis calls with personal identifier contained in the OpenID'''
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>{ATTRIBUTE_SERVICE_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>{MYPROXY_SERVICE_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>{SLCS_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>{OAUTH_ACCESS_TOK_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>{OAUTH_RESOURCE_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>{OAUTH_AUTHORIZE_URI}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
   </XRD>
</xrds:XRDS>
'''

@app.route('/openid/')
def yadis_general_response():
    """Generic response for Yadis call where the OpenID is generalised for the IdP and
    contains no personal identifier"""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>{ATTRIBUTE_SERVICE_URI}</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>{MYPROXY_SERVICE_URI}</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>{SLCS_URI}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>{OAUTH_ACCESS_TOK_URI}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>{OAUTH_RESOURCE_URI}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>{OAUTH_AUTHORIZE_URI}</URI>
        </Service>
   </XRD>
</xrds:XRDS>
'''
