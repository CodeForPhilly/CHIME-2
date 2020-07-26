# -*- coding: utf-8 -*-
"""CSV upload service."""
import base64
import datetime
import io

import dash_html_components as html
import dash_table
import pandas as pd


def parse_contents(contents, filename, date):
    """
    Parse the contents of a csv.

    :param contents: Contents of the file.
    :type contents: basestring

    :param filename: Name of uploaded file.
    :type filename: str

    :param date: Upload date.
    :type date: str

    :return: Dash datatable object.
    """
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return html.Div(
        className="container",
        children=[
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),
            dash_table.DataTable(
                data=df.to_dict("records"),
                columns=[{"name": i, "id": i} for i in df.columns],
                style_table={"overflowX": "auto"},
                style_cell={
                    "height": "auto",
                    # all three widths are needed
                    "minWidth": "180px",
                    "width": "180px",
                    "maxWidth": "180px",
                    "whiteSpace": "normal",
                },
            ),
            html.Hr(),  # horizontal line
            # For debugging, display the raw contents provided by the web browser
            html.Div("Raw Content"),
            html.Pre(
                contents[0:200] + "...",
                style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
            ),
        ],
    )
