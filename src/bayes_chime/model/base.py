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
    _model_parameters: Dict[str, List[str]] = {"compartments": [],
                                               "epidemiological": [],
                                               "regional": []
                                               }

    def _verify_legal_params(self, parameters: Dict[str, Any], ) -> None:
        """Verify that the list of parameters passed by the parameters
        object is legal for the selected model

        :raises ModelError:
            If any of parameters not found in _model_parameters
        """
        for parameter in parameters:
            if parameter not in self._model_parameters:
                raise ModelError(f"'{parameter}' not valid selection")

    def _set_compartments(
        self, parameters: Dict[str, Any],
    ) -> None:
        """Parse the defined legal parameters for compartments and set
        the compartments as class attributes with values equal to those
        defined by the parameters object"""
        for compartment in self._model_parameters["compartments"]:
            self.__set_attr__ = (compartment, parameters[compartment])

    def __init__(self, distributions: str = "normal") -> None:
        self._dist = distributions

    @abstractmethod
    def fit(self, parameters: Dict[str, Any]) -> None:
        """Fit the model to the parameters"""

    def _n_from_compartments(self):
        return sum(
            getattr(self, compartment)
            for compartment in self._model_parameters["compartments"]
        )

    @abstractmethod
    def simulate(self):
        """Execute a single model step"""
