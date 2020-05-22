# -*- coding: utf-8 -*-
"""
helper functions for model classes
"""
import datetime as dt
from typing import Dict, List

from ._config import DATE_FORMAT


def _n_from_compartments(compartments: List[str]) -> int:
    """Return the combined sum of all compartments"""
    return sum(compartments)


def str_to_datetime(pattern: str) -> dt.datetime:
    """Cast an iso formatted string to datetime"""
    return dt.datetime.strptime(pattern, DATE_FORMAT)
