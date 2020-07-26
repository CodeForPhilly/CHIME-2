# -*- coding: utf-8 -*-
"""Parameter Input Component."""
from typing import Union

import dash_bootstrap_components as dbc
import dash_html_components as html


class ParameterInput(object):
    """Parameter input class to simplify input component creation."""

    def __init__(self, title: str, dtype: Union[int, float],) -> None:
        """ # noqa

        :param title: Component name
        :type title: str

        :param dtype: Parameter data type
        :type dtype: str
        """
        self.title = title
        self.dtype = dtype

    @property
    def html(self):
        """Return the generated component."""
        return [
            html.P(f"{self.title}", style={"text-align": "center"}),
            dbc.Input(),
            html.Br(),
        ]
