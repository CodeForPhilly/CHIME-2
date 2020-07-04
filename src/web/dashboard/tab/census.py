import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

df = pd.read_csv(
    "https://raw.githubusercontent.com/pennsignals/chime_sims/master/data/CCH_ts.csv"
)

tab_layout = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row([
                dbc.Col([
                    dbc.Input()
                ])
            ])
        ]
    )
)
