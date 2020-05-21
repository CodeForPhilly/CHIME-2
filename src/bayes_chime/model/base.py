# -*- coding: utf-8 -*-
""".. currentmodule:: bayes_chime:

Base class for compartment models.
"""
from abc import abstractmethod
from collections import namedtuple
import datetime as dt
from typing import Any, Dict, List, Union

import numpy as np

_valid_parameters: Dict[str, List[str]] = {"datetime": [],
                                           "compartments": [],
                                           "epidemiological": [],
                                           "regional": []
                                           }


class ModelError(AttributeError, NameError, KeyError):
    """Exception class for model.

     extends:
        ``AttributeError``, ``NameError``, ``KeyError``
    """


def _get_valid_parameters(valid_parameters: Dict[str, List[str]]) -> List[str]:
    """Get a list of valid parameters from the model parameters object"""
    parameter_list = []
    for parameter_group, parameters in valid_parameters.items():
        parameter_list += parameters
    return parameter_list


def _n_from_compartments(compartments: Dict[str, List[int]]) -> int:
    """Return the combined sum of the items in the last index position"""
    return sum(value[-1] for c, value in compartments.items())


def str_to_datetime(pattern: str) -> dt.datetime:
    """Cast an iso formatted string to datetime"""
    return dt.datetime.strptime(pattern, "%Y-%m-%d")  # TODO : Move date format to user config


class CompartmentalModel(object):
    """:class: CompartmentalModel
    ==================
    CompartmentalModel
    ==================

    Base class for the various models used by the CHIME simulation.
    ..
    Attributes:
    ----------

        :_idx:
            A numpy array start = 0, stop = number of days simulation is ran
            step = 1
        :_dist:
            the type of distribution to use for model parameters
        :compartments_:
            Dictionary with compartment names as keys and arrays containing
            population counts for each compartment
        :_model_parameters:
            This is a dictionary which defines the valid parameters for each
            parameter group.

    Methods
    -------

        - _get_compartments

    Abstract Methods
    -------

        - CompartmentModel.fit(self, parameters, census)

        - CompartmentModel.simulate(self)
    """

    _idx: np.ndarray = None
    _compartments: Dict[str, List[int]] = {}
    _model_parameters: Dict[str, List[str]] = {}

    def __init__(self, distributions: str = "normal") -> None:
        self._dist = distributions

    @abstractmethod
    def fit(
        self, parameters: Dict[str, Any], census: np.ndarray = None
    ) -> None:
        """Fit the model to the parameters"""

    @abstractmethod
    def simulate(self):
        """Execute a single model step"""

    def _verify_legal_params(self, submitted_params: Dict[str, Any],) -> None:
        """Check all required parameters are present"""
        for parameter in submitted_params:
            if parameter not in self._model_parameters:
                raise ModelError(f"'{parameter}' not valid selection")

    def _get_compartments(
        self, parameters: Dict[str, Any],
    ) -> Dict[str, List[int]]:
        """Parse the compartments and values from the parameter object"""
        return {compartment: [
            int(parameters[compartment])
        ] for compartment in self._model_parameters["compartments"]}




