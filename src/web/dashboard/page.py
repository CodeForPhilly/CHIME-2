import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .component import navbar, header
from . import tab


layout = html.Div([navbar.content, header.content, tab.content,])
