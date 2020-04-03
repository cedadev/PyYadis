# PyYadis

Simple Flask app to implement the Yadis discovery protocol serve an XRDS 
document containing service endpoints.  Developed for Earth System Grid 
Federation.


* Free software: BSD - see LICENSE file in top-level package directory

## Configuration
Configuration can be set by passing a dictionary to the `YadisFlaskApp.create`
method:

```python
cfg = {
    'OPENID_URI_PATH_PREFIX': _OPENID_URI_PATH_PREFIX,
    'ATTRIBUTE_SERVICE_URI': 'https://<host>/attribute-service/',
    'MYPROXY_SERVICE_URI': 'socket://<host>:7512',
    'SLCS_URI': 'https://<host>/onlineca/certificate/',
    'OAUTH_ACCESS_TOK_URI': 'https://<host>/oauth/access_token',
    'OAUTH_RESOURCE_URI': 'https://<host>/oauth/certificate/',
    'OAUTH_AUTHORIZE_URI': 'https://<host>/oauth/authorize'
}
app = YadisFlaskApp.create(config=cfg)
```

Alternatively, create a Python module to contain the configuration settings.  An example is 
provided in `yadis_server.config`:

```python
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

The environment variable `YADIS_FLASK_APP_CFG_FILEPATH` must be set to the 
location of the configuration module.

By default the application will load the template file in the package 
`yadis_server/templates/yadis.xml`.  This can be overridden using the environment
variable, `YADIS_FLASK_APP_TMPL_DIR`.  The template file can changed as needed and
alternative or additional configuration variables set.

## To run
The application can be run with for example `waitress`:

```bash
$ export YADIS_FLASK_APP_CFG_FILEPATH=<config file path>
$ waitress-serve --call 'yadis_server:create_app'
```

Where `YADIS_FLASK_APP_CFG_FILEPATH` is set to the location of a configuration file containing the settings for the service endpoints to be included in the XRDS.

## Testing
Start the service following the instructions in the previous section and then invoke using for example `curl`.

Generic response:

```bash
$ curl http://localhost:8080/esgf-idp/openid/
<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>https://somesite.ac.uk/attribute-service/</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>socket://somesite.ac.uk:7512</URI>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>https://somesite.ac.uk/onlineca/certificate/</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>https://somesite.ac.uk/oauth/access_token</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>https://somesite.ac.uk/oauth/certificate/</URI>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>https://somesite.ac.uk/oauth/authorize</URI>
        </Service>
   </XRD>
</xrds:XRDS>
```

Identity Response:

```bash
curl http://localhost:8080/esgf-idp/openid/j.bloggs
<?xml version="1.0" encoding="UTF-8"?>
<xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)">
    <XRD>
        <Service priority="20">
            <Type>urn:esg:security:attribute-service</Type>
            <URI>https://somesite.ac.uk/attribute-service/</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:myproxy-service</Type>
            <URI>socket://somesite.ac.uk:7512</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
        <Service priority="10">
            <Type>urn:esg:security:slcs</Type>
            <URI>https://somesite.ac.uk/onlineca/certificate/</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:access</Type>
            <URI>https://somesite.ac.uk/oauth/access_token</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:resource</Type>
            <URI>https://somesite.ac.uk/oauth/certificate/</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
        <Service priority="5">
            <Type>urn:esg:security:oauth:endpoint:authorize</Type>
            <URI>https://somesite.ac.uk/oauth/authorize</URI>
            <LocalID>http://localhost:8080/esgf-idp/openid/j.bloggs</LocalID>
        </Service>
   </XRD>
</xrds:XRDS>
```
