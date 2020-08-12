# -*- coding: utf-8 -*-
"""Main library interface.
"""
from collections import namedtuple

_valid_parameters: List[str] = []


class CHIME2(object):
    """Class representation of CHIME-2 from Penn Medicine."""

    def __init__(self) -> None:
        self._ts = None
        self._params = None

    def fit(self, data: Dict[str, Dict[str, str]]) -> None:

        self._params = data["parameter"]
