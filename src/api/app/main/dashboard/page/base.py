# -*- coding: utf-8 -*-
"""
Base class for pages
"""
from abc import abstractmethod
from typing import List

from dash.development.base_component import ComponentMeta

from app.main.dashboard.component.base import HTMLComponentError


class PageLoadError(HTMLComponentError, LookupError):
    """Exception to be thrown for page errors"""


class Page:
    """
    Page base class. Defines page layout, combines view, model and
    controller.
    """
    _layout = None

    def __init__(self):
        self._layout = self._get_layout()

    @abstractmethod
    def _get_layout(self):
        """Method to overload"""

    @property
    def layout(self):
        """Accessor for page layout"""
        return self._layout

