# -*- coding: utf-8 -*-
"""

"""
import dash_core_components as dcc
import dash_html_components as html


def build_tabs():
    """Build the tabs for the dashboard front page"""
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        # intro / about
                        id="intro-tab",
                        label="CHIME 2",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        # set parameters
                        id="parameters-tab",
                        label="Model Parameters",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        # upload csv / dash_table
                        id="census-tab",
                        label="Census Data",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        # model selection / hyperparameters
                        id="model-configuration-tab",
                        label="Model Configuration",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )
