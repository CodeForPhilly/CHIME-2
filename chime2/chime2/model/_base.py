# -*- coding: utf-8 -*-
"""
"""
from abc import abstractmethod
from typing import List

_legal_pathogens: List[str] = ["covid"]


def _get_compartments(model_compartments: set) -> dict:
    return {key: list() for key in model_compartments}


def _get_pathogen(pattern: str) -> object:
    p = pattern.lower()
    if p not in _legal_pathogens:
        raise NotImplementedError(f"'{p}' not currently implemented.")
    if p == "covid":
        from chime2.pathogen.viral import Covid19

        return Covid19()


class CompartmentalModel(object):
    """Base class for compartmental models."""

    def __init__(
        self, compartments: set, pathogen: str,
    ):

        self._compartments = _get_compartments(model_compartments=compartments)
        self._pathogen = _get_pathogen(pattern=pathogen)

    @abstractmethod
    def step(self):
        """Abstract method for overloading"""

    @property
    def compartments(self):
        return self._compartments

    @property
    def pathogen(self):
        return self._pathogen

    def __iter__(self):
        self.step()
