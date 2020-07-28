# -*- coding: utf-8 -*-
"""Page layout."""
import dash_core_components as dcc
import dash_html_components as html

from . import tab
from .component import header

layout = html.Div([header.content, dcc.Graph(), tab.content])
