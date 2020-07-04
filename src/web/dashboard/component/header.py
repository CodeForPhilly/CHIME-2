import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.server.model.user import load_user

welcome = html.H1([
    "Welcome back to CHIME2"
])

user = html.Div(
    children=[
        html.Div(id='header_current_user'),
        html.Div(id='header_user_output', children='xxxx')
    ],
)

content = dbc.Jumbotron([
    welcome,
    user,
    dbc.Card(
        [
            dbc.CardImg(src="", top=True),
            dbc.CardBody(
                [
                    dbc.Button(
                        "Go to your dashboard", href="/dashboard/", color="primary"
                    ),
                ]
            ),
        ],
        className="w-75 mb-3",
    ),
    dcc.Markdown("Lorizzle Ipsizzle"),
]
)
