# -*- coding: utf-8 -*-
"""Parameters tab."""
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app.dashboard.component import build_parameter_inputs

input_groups = build_parameter_inputs()


tab_header = dcc.Markdown(
    """
----
More information / instructions about using model parameters here.
----
"""
)

row = html.Div(
    className="card-deck",
    children=[param_group.container for param_group in input_groups.values()],
)

tab_layout = dbc.Card(dbc.CardBody([tab_header, row]))
