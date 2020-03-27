# -*- coding: utf-8 -*-

"""Flask callbacks for returning Yadis responses."""
__author__ = """Philip Kershaw"""
__contact__ = "philip.kershaw@stfc.ac.uk"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
import os

from flask import Flask, request, Response
from flask.templating import render_template


class YadisFlaskAppConfigError(Exception):
    '''Configuration error loading Yadis Flask App'''
    
    
class YadisFlaskApp:
    RESPONSE_TYPE = 'application/xrd+xml'
    CFG_FILEPATH_ENVVARNAME = 'YADIS_FLASK_APP_CFG_FILEPATH'
    TMPL_DIRPATH_ENVVARNAME = 'YADIS_FLASK_APP_TMPL_DIR'
    TMPL_FILENAME = 'yadis.xml'
    
    @classmethod
    def create(cls, config=None):
        tmpl_dir = os.getenv('YADIS_FLASK_APP_TMPL_DIR')
        flask_extra_args = {}
        if tmpl_dir:
            # Check template is present otherwise we won't know until a client
            # tries the Yadis link
            tmpl_filepath = os.path.join(tmpl_dir, cls.TMPL_FILENAME)
            if not os.path.isfile(tmpl_filepath):
                raise YadisFlaskAppConfigError(
                    'Error loading template file.  Check that the "'
                    f'{cls.TMPL_DIRPATH_ENVVARNAME}" environment variable is '
                    'set to a valid directory containing the template file '
                    f'"{cls.TMPL_FILENAME}" with the correct access '
                    'permissions')
            
            flask_extra_args.update({'template_folder': tmpl_dir})
            
        app = Flask(__name__, instance_relative_config=True,
                    **flask_extra_args)
        
        if config is not None:
            app.config.update(config)    
        else:
            app.config.from_envvar(cls.CFG_FILEPATH_ENVVARNAME)

        @app.route(f'{app.config["OPENID_URI_PATH_PREFIX"]}/<username>')
        def yadis_personal_response(username):
            '''Respond to Yadis calls with personal identifier contained in the 
            OpenID'''
            return Response(render_template(cls.TMPL_FILENAME, app=app, 
                                            user_uri=request.url), 
                            mimetype=cls.RESPONSE_TYPE)
        
        @app.route(f'{app.config["OPENID_URI_PATH_PREFIX"]}/')
        def yadis_general_response():
            """Generic response for Yadis call where the OpenID is generalised 
            for the IdP and contains no personal identifier"""
            return Response(render_template(cls.TMPL_FILENAME, app=app), 
                            mimetype=cls.RESPONSE_TYPE)
            
        return app

