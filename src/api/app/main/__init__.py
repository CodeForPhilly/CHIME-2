# -*- coding: utf-8 -*-
"""
====
main
====

Creates flask backend pushes Dash app as app context
"""
from flask import Flask

from app.config import config_from_object
from app.main.extensions import db, encrypt

# from app.assets import compile_assets
# from app.main.dashboard import create_dashboard

config = config_from_object()


def create_app(env):
    """Create the flask instance"""
    server = Flask(__name__)
    server.config.from_object(env)
    db.init_app(server)
    encrypt.init_app(server)

    with server.app_context():
        from app.main.dashboard import create_dashboard

        app = create_dashboard(env=env, server=server)
        # compile_assets(app)

        return app
