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
    """Base class for the various models used by the CHIME simulation."""

    @abstractmethod
    def fit(self) -> None:
        """Fit the model to the parameters"""

    @abstractmethod
    def simulate(self):
        """Execute a single model step"""
