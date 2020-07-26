# -*- coding: utf-8 -*-
"""Parameters tab."""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/pennsignals/chime_sims/master/data/CCH_parameters.csv"
)

header = dcc.Markdown(
    """
# Model Parameters
----
More info about model parameters / instructions
"""
)

tab_header = dcc.Markdown(
    """
----
More information / instructions about using model parameters here.
----
"""
)

row = html.Div([dbc.Row([]),])  # noqa

tab_layout = dbc.Card(dbc.CardBody([tab_header, row]))
