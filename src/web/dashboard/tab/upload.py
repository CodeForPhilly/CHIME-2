import dash_core_components as dcc
import dash_html_components as html

from app.dashboard.component import upload

tab_layout = html.Div(
    [
        html.H3("Upload files here."),
        dcc.Markdown(
            """
    Upload instructions go here.
    """
        ),
        upload.button,
    ]
)
