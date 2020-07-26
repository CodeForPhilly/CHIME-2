# -*- coding: utf-8 -*-
"""Dashboard built using plotly-dash."""
import dash
from dash_bootstrap_components.themes import BOOTSTRAP

from app.dashboard import page
from app.dashboard.customization import custom_index_str
from app.settings import ROOT_PATH


def register_dashboard(app):
    """Dash application factory."""
    # from .callback import register_callbacks

    external_stylesheets = [
        BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;1,400;1,600&display=swap",
    ]
    # Javascript scripts TODO: Inject CSRF token
    external_scripts = [str(ROOT_PATH + "/static/main_js.bundle.js")]
    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    dashboard = dash.Dash(
        __name__,
        server=app,
        # url_base_pathname="/dashboard/",
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        url_base_pathname="/dashboard/",
        assets_folder=ROOT_PATH + "/static/build/img/",
        meta_tags=[meta_viewport],
        index_string=custom_index_str,
        suppress_callback_exceptions=True,
    )

    with app.app_context():
        from app.dashboard.callback import register_callbacks

        dashboard.layout = page.layout
        register_callbacks(dashboard=dashboard)

    # _protect_dashboard(dashboard)


# def _protect_dashboard(dashboard):
#     for view_func in dashboard.server.view_functions:
#         if view_func.startswith(dashboard.config.url_base_pathname):
#             dashboard.server.view_functions[view_func] = login_required(
#                 dashboard.server.view_functions[view_func])
#             )
