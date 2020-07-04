from typing import Union

import dash_html_components as html
import dash_bootstrap_components as dbc


class ParameterInput(object):
    """
    """

    def __init__(self,
                 title: str,
                 dtype: Union[int, float],
                 ) -> None:
        self.title = title
        self.dtype = dtype

    @property
    def html(self):
        return [
            html.P(f"{self.title}",
                   style={'text-align': 'center'}),
            dbc.Input(),
            html.Br()
        ]
