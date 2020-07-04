import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.dashboard.component.parameter import ParameterInput

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

epidemiological_column = dbc.Col(
    [html.H5("Epidemiological",
             style={"text-align": "center",
                    "text-decoration": "underline"
                    }
             )] +
    ParameterInput(title="Incubation Days", dtype=int).html +
    ParameterInput(title="Recovery Days", dtype=int).html,
    width=2
)

regional_column = dbc.Col(
    [html.H5("Region",
             style={"text-align": "center",
                    "text-decoration": "underline"
                    }
             )] +
    ParameterInput(title="Regional Population", dtype=int).html +
    ParameterInput(title="Market Share", dtype=float).html +
    ParameterInput(title="Day One Hospitalized", dtype=int).html +
    ParameterInput(title="Bed Capacity", dtype=int).html +
    ParameterInput(title="Ventilator Capacity", dtype=int).html,
    width=2
)

interventions_column = dbc.Col(
    # Proportion inputs
    [html.H5("Interventions",
             style={"text-align": "center",
                    "text-decoration": "underline"
                    })] +
    ParameterInput(title="Hospitalized", dtype=float).html +
    ParameterInput(title="Intensive Care", dtype=float).html +
    ParameterInput(title="Ventilatory", dtype=float).html +
    # Lengths of stay inputs
    [html.H5("Lengths of Stay",
             style={"text-align": "center",
                    "text-decoration": "underline"
                    }
             )] +
    ParameterInput(title="Hospitalized", dtype=int).html +
    ParameterInput(title="Intensive Care", dtype=int).html +
    ParameterInput(title="Ventilatory", dtype=int).html,
    width=2
)

row = html.Div(
    [
        dbc.Row(
            [
                epidemiological_column,
                regional_column,
                interventions_column,
            ]
        ),
    ]
)

tab_layout = dbc.Card(
    dbc.CardBody(
        [
            tab_header,
            row
        ]
    )
)
