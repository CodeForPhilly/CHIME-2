"""
Dashboard
=========

This dashboard created using Plotly's Dash framework, which combines
flask and react to create interactive dashboards optimal for uses such
as this one. For specific information about Plotly Dash seek out their
documentation which is available `here. <https://dash.plot.ly>`_

The dashboard structure follows Model-View-Controller design pattern,
as well SOLID, YAGNI, and KISS design principles. For information
about MVC component please seek out the documentation in the respective
module.

---
__
Modules
~~~~~~~

callback:
    (controller) responsible for orchestrating interaction between model
    and view

component:
    (view) individual pieces of a page layout

page:
    dashboard layout defined here

service:
    (model) short-lived data manipulations which are triggered by
    callbacks
"""
from typing import Any, List, NewType

from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

FlaskServer = NewType("FlaskServer", object)

_google_stylesheet = (
    "https://fonts.googleapis.com/",
    "css2?family=Open+Sans:ital,wght@0,400;",
    "0,600;1,400;1,600&display=swap",
)


class Dashboard(object):
    """Interactive dashboard presenting chime2"""

    style: List[Any] = [BOOTSTRAP, _google_stylesheet]  # External CSS stylesheets
    scripts: List[str] = []  # Additional JS files to load with app

    def __init__(self, server, url_path: str = "/dashboard/") -> None:
        self._dash = Dash(
            __name__,
            server=server,
            assets_folder="assets",
            external_stylesheets=self.style,
            external_scripts=self.scripts,
            url_base_pathname=url_path,
        )

    @property
    def build(self):
        return self._dash
