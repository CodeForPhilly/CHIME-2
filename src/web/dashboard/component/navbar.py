import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


content = dbc.NavbarSimple(
    children=[
        dbc.NavLink("Updates", href="/updates/"),
        dbc.NavLink("GitHub", href="https://github.com/CodeForPhilly/CHIME-2/"),
        dbc.DropdownMenu(
            children=[dbc.DropdownMenuItem("logout", href="/logout")],
            nav=True,
            in_navbar=True,
            label="account",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Code for Philly", href="/logout"),
                dbc.DropdownMenuItem(
                    "Predictive Healthcare",
                    href="http://predictivehealthcare.pennmedicine.org/",
                ),
            ],
            nav=True,
            in_navbar=True,
            label="more",
        ),
    ],
    brand="U Penn CHIME2",
    brand_href="#",
    color="primary",
    dark=True,
)
