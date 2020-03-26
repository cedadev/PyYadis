# -*- coding: utf-8 -*-

"""Flask callbacks for returning Yadis responses."""
from flask.templating import render_template

__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from flask import Flask, request, Response


class YadisFlaskAppConfigError(Exception):
    "Error with configuration settings for Yadis Flask application"


class YadisFlaskApp:
    CFG_FILEPATH_ENVVARNAME = 'YADIS_FLASK_APP_CFG_FILEPATH'
    RESPONSE_TYPE = 'application/xrd+xml'
    TMPL_FILENAME = 'yadis.xml'
    
    @classmethod
    def create(cls, config=None):
        app = Flask(__name__, instance_relative_config=True)
        
        if config is not None:
            app.config.update(config)
            
        elif not app.config.from_envvar(cls.CFG_FILEPATH_ENVVARNAME):
            # Set configuration from a separate module 
            raise YadisFlaskAppConfigError(f'Error loading config file path '
                                           'Please check the "{cls.CFG_FILEPATH_ENVVARNAME}"'
                                           'environment variable is set to valid file')
        
        @app.route(f'{app.config["OPENID_URI_PATH_PREFIX"]}/<username>')
        def yadis_personal_response(username):
            '''Respond to Yadis calls with personal identifier contained in the OpenID'''
            return Response(render_template(cls.TMPL_FILENAME, app=app, user_uri=request.url), 
                            mimetype=cls.RESPONSE_TYPE)
        
        @app.route('/openid/')
        def yadis_general_response():
            """Generic response for Yadis call where the OpenID is generalised for the IdP and
            contains no personal identifier"""
            return Response(render_template(cls.TMPL_FILENAME, app=app), 
                            mimetype=cls.RESPONSE_TYPE)
            
        return app


def create():
    '''Convenience factory function for use with waitress e.g.
    
    `% waitress-serve --call 'yadis_server:flask_app.create`
    '''
    return YadisFlaskApp.create()


if __name__ == "__main__":
    YadisFlaskApp.create().run()