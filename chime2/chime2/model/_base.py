# -*- coding: utf-8 -*-
"""
"""


def _get_compartments(model_compartments: set) -> dict:
    return {key: list() for key in model_compartments}


class CompartmentalModel(object):
    """Base class for compartmental models."""

    def __init__(self, compartments: set):

        self._compartments = _get_compartments(model_compartments=compartments)

