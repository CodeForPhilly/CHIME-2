from flask import session
from dash.dependencies import Input, Output, State

from .tab import parameter, census, upload, report
from .service.upload import parse_contents


def register_callbacks(dashboard):
    @dashboard.callback(
        Output("card-content", "children"), [Input("card-tabs", "active_tab")]
    )
    def tab_content(active_tab):
        if active_tab == "parameter-tab":
            return parameter.tab_layout
        elif active_tab == "census-tab":
            return census.tab_layout
        elif active_tab == "upload-tab":
            return upload.tab_layout
        elif active_tab == "report-tab":
            return report.tab_layout

    @dashboard.callback(
        Output("output-data-upload", "children"),
        [Input("upload-data", "contents")],
        [State("upload-data", "filename"), State("upload-data", "last_modified")],
    )
    def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [
                parse_contents(c, n, d)
                for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
            ]
            return children

    @dashboard.callback(
        Output('header_current_user', 'children'),
        [Input('header_user_output', 'children')])
    def get_session_user(children):
        return session.get('username', None)
