# -*- coding: utf-8 -*-
"""Base class for components
"""
from collections import namedtuple
from typing import List

from dash.development.base_component import ComponentMeta
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

_component_registry: List[str] = []


class HTMLComponentError(AttributeError, KeyError, LookupError):
    """Custom exception for errors when rendering component html."""


class Component:
    """Base class for components."""

    def __init__(self):
        self._html = None


    @property
    def component(self) -> List[ComponentMeta]:
        """Accessor for `get_html` wrapped with Exception handling:

        Raises:
            HTMLComponentError: if any error occurs.
        """
        if self._html is None:
            try:
                self._html = self.get_html()
            except Exception as error:
                raise HTMLComponentError(error)
        return self._html

    def get_html(self):
        return html.Div("")
