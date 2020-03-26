# -*- coding: utf-8 -*-

"""Flask callbacks for returning Yadis responses."""

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from flask import Flask, escape, request, Response
from markupsafe import escape


class YadisFlaskAppConfigError(Exception):
    "Error with configuration settings for Yadis Flask application"


app = Flask(__name__)

# Set configuration from a separate module 
if not app.config.from_envvar('YADIS_FLASK_APP_CFG_FILEPATH'):
    raise YadisFlaskAppConfigError('Error loading config file path '
                                   'Please check the "YADIS_FLASK_APP_CFG_FILEPATH"'
                                   'environment variable is set to valid file')


@app.route(f'{app.config["OPENID_URI_PATH_PREFIX"]}/<username>')
def yadis_personal_response(username):
    '''Respond to Yadis calls with personal identifier contained in the OpenID'''
    return Response(f'''<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>{app.config["ATTRIBUTE_SERVICE_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>{app.config["MYPROXY_SERVICE_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>{app.config["SLCS_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>{app.config["OAUTH_ACCESS_TOK_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>{app.config["OAUTH_RESOURCE_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>{app.config["OAUTH_AUTHORIZE_URI"]}</URI>
            <LocalID>{request.url}</LocalID>
        </Service>
   </XRD>
</xrds:XRDS>
''', mimetype='text/xml')

@app.route('/openid/')
def yadis_general_response():
    """Generic response for Yadis call where the OpenID is generalised for the IdP and
    contains no personal identifier"""
    return Response(f'''<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>{app.config["ATTRIBUTE_SERVICE_URI"]}</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>{app.config["MYPROXY_SERVICE_URI"]}</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>{app.config["SLCS_URI"]}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>{app.config["OAUTH_ACCESS_TOK_URI"]}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>{app.config["OAUTH_RESOURCE_URI"]}</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>{app.config["OAUTH_AUTHORIZE_URI"]}</URI>
        </Service>
   </XRD>
</xrds:XRDS>
''', mimetype='text/xml')


