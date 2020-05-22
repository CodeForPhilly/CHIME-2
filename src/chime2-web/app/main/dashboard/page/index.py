# -*- coding: utf-8 -*-
"""
Dashboard front page
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.main.dashboard.component.navbar import Navbar
from app.main.dashboard.page.base import Page


nav = Navbar()

class Index(Page):
    """
    """
    components = None

    def __init__(self):
        """
        """
        super().__init__()
        self.components = {"navbar": nav}

    def _get_layout(self):
        """Initializes the content container dash html
        """
        content = html.Main(
            className="py-5",
            children=[dbc.Container(
                children=nav.component
            )])

        return [content]
