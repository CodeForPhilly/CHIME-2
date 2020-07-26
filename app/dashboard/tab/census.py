import dash_table
import dash_bootstrap_components as dbc


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
