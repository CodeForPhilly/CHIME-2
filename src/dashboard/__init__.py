import dash

from flask.helpers import get_root_path
from flask_login import login_required
from dash_bootstrap_components.themes import BOOTSTRAP

from . import page


def register_dashboard(app):
    # from .callback import register_callbacks

    external_stylesheets = [
        BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;1,400;1,600&display=swap",
    ]
    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    dashboard = dash.Dash(
        __name__,
        server=app,
        url_base_pathname="/dashboard/",
        assets_folder=get_root_path(__name__) + "/assets/",
        external_stylesheets=external_stylesheets,
        meta_tags=[meta_viewport],
    )

    with app.app_context():
        dashboard.title = "CHIME-2"
        dashboard.layout = page.layout
        # register_callbacks(dashboard)

#     _protect_dashboard(dashboard)
#
#
# def _protect_dashboard(dashboard):
#     for view_func in dashboard.server.view_functions:
#         if view_func.startswith(dashboard.config.url_base_pathname):
#             dashboard.server.view_functions[view_func] = login_required(
#                 dashboard.server.view_functions[view_func]
#             )
