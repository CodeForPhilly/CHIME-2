""".. currentmodule:: bayes_chime:

Base class for compartment models.
"""
from abc import abstractmethod
from collections import namedtuple
from typing import Any, Dict, List

_models: List[str] = []


class ModelError(AttributeError, NameError, KeyError):
    """Exception class for model.

     extends:
        ``AttributeError``, ``NameError``, ``KeyError``
    """


class CompartmentalModel(object):
    """Base class for the various models used by the CHIME
     simulation."""

    _valid_parameters: Dict[str, Any] = {}
    _compartments: List[str] = []  # TODO : Compartments as objects

    @abstractmethod
    def fit(self, **parameters: Dict[str, Any]):
        """Fit the model"""

    @abstractmethod
    def simulate(self):
        """Execute a single model step"""


