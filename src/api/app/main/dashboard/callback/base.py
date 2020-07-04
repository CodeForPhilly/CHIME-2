# -*- coding: utf-8 -*-
"""
Base class for callbacks
"""
from collections import namedtuple

from dash.dependencies import Input, Output


RegisteredCallback = namedtuple("RegisteredCallback", "callback component")

_callback_registry: Dict[str, RegisteredCallback] = []

class AppCallback:
    """
    Base class for Dash app callbacks
    """
    _associated_components: List[ComponentMeta] = []

    def __init_subclass__(cls, **kwargs):
        if not kwargs["_associated_components"]:
            raise AttributeError(
                "Callbacks must have at least one associated component"
            )

    @abstractmethod
    def _set_callback(self):

