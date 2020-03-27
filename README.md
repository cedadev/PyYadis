# PyYadis

Simple Flask app to implement the Yadis discovery protocol serve an XRDS document containing service endpoints.  Developed for Earth System Grid Federation


* Free software: BSD - see LICENSE file in top-level package directory

## Configuration
Create a Python module to contain the configuration settings.  An example is provided in `yadis_server.config`:

```
# Path prefix for OpenID URIs.  ESGF stock implementation uses
OPENID_URI_PATH_PREFIX = '/esgf-idp/openid/'

# CEDA implementation uses this prefix
#OPENID_URI_PATH_PREFIX = '/openid/'

# Sample settings for ESGF XRDS
ATTRIBUTE_SERVICE_URI = 'https://<host>/attribute-service/'
MYPROXY_SERVICE_URI = 'socket://<host>:7512'
SLCS_URI = 'https://<host>/onlineca/certificate/'
OAUTH_ACCESS_TOK_URI = 'https://<host>/oauth/access_token'
OAUTH_RESOURCE_URI = 'https://<host>/oauth/certificate/'
OAUTH_AUTHORIZE_URI = 'https://<host>/oauth/authorize'
```

The environment variable `YADIS_FLASK_APP_CFG_FILEPATH` must be set to the location of the configuration module.

## To run

```
$ export YADIS_FLASK_APP_CFG_FILEPATH=<config file path>
$ waitress-serve --call 'yadis_server:create_app.'
```

Where `YADIS_FLASK_APP_CFG_FILEPATH` is set to the location of a configuration file containing the settings for the service endpoints to be included in the XRDS.
