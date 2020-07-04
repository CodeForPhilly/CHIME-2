# -*- coding: utf-8 -*-
"""
1
"""

import dash
from .page.index import Index
from .component.navbar import Navbar
from app.main import config

homepage = Index()
nav = Navbar()


def create_dashboard(env, server):
    """Create the dashboard instance"""
    dashboard = dash.Dash(
        __name__,
        server=server,
        external_stylesheets=env.dash_stylesheets,
        external_scripts=env.dash_scripts,
        routes_pathname_prefix=env.dashboard_route,
        assets_folder=config.assets_path
    )
    dashboard.layout = nav.component

    return dashboard.server
