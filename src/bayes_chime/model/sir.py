"""model/sir.py
===
SIR
===

SIR Compartmental Model

TODO : Documentation
TODO : Unit testing

"""
from typing import Any, List, Dict, NewType

from .base import CompartmentalModel
from src.bayes_chime.util import _n_from_compartments

import numpy as np

_valid_distributions: List[str] = ["normal"]
_sir_params: Dict[str, Any] = {
    "compartments": ["susceptible", "infected", "removed"],
    "epidemiological": ["beta", "gamma"]
}


class SIR(CompartmentalModel):
    """
    =======================
    SIR Compartmental Model
    =======================

    # TODO summary explanation, args, attrs, methods
    """
    beta: float
    gamma: float
    susceptible: int
    infected: int
    removed: int

    def __init__(self):
        super().__init__()
        self._model_parameters = _sir_params
        self._set_compartments(self._model_parameters)

    # calculations for missing values 🡇
    def _get_gamma(self, parameters):
        if not self.gamma:
            self.gamma = 1 / (
                parameters["recovery_days"] / parameters["days_per_step"]
            )

    def _get_beta(self, parameters) -> None:
        if not self.beta:
            total_population = _n_from_compartments()
            b = np.log(2) / (parameters["initial_doubling_time"] / 1)
            b += self.gamma
            b *= total_population / parameters["initial_susceptible"]
            self.beta = b

    def fit(self, parameters: Dict[str, Any]) -> None:
        """
        Fit the model to the time series data provided by hospital
        census records. Find missing values for `gamma` and `beta` if
        none exist.

        :argument parameters:
            Dictionary object of parameters to fit.
        """
        self._verify_legal_params(parameters)
        if "gamma" not in parameters:
            self._get_gamma(parameters)
        if "beta" not in parameters:
            self._get_beta(parameters)
        for compartment in self._model_parameters["compartments"]:
            setattr(self, compartment, parameters[compartment])

    @property
    def total(self):
        """Total population of all compartments"""
        return _n_from_compartments(self._model_parameters["compartments"])

    def _d_si(self):
        """Count newly infected"""
        n = self.total
        return self.beta * self.susceptible / n * self.infected

    def _d_ir(self):
        """Determine new recovered"""
        return self.gamma * self.infected

    def _scale_compartments(self, scalar):
        for compartment in self._model_parameters["compartments"]:
            self.__set_attr__(compartment, max((compartment * scalar), 0))

    def simulate(self) -> np.array:
        """Calculates the results of the model"""
        """
        Execute simulation
        """
        starting_total = self.total

        self.susceptible -= round(self._d_si())
        self.infected += round(self._d_si()
                               - self._d_ir())
        self.removed += round(self._d_si())

        scalar = starting_total / self.total
        self._scale_compartments(scalar)

        return {
            "susceptible": self.susceptible,
            "infected": self.infected,
            "removed": self.removed,
            "infected_new": self._d_si() * scalar,
            "recovered_new": self._d_ir() * scalar,
        }
        # _validate_parameters(parameters, self._model_parameters)
        # self._idx = _build_dt_index(
        #     parameters["dates"]["start_date"], parameters["dates"]["stop_date"]
        # )
        # if "compartments" not in parameters:
        #     raise ModelError("Parameters missing compartments")
        # self.compartments_ = _get_compartments(
        #     self._model_parameters["compartments"],
        #     parameters["compartments"]
