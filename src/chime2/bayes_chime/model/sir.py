"""model/sir.py
===
SIR
===

SIR Compartmental Model

TODO : Documentation
TODO : Unit testing

"""
from typing import Any, List, Dict

from ._base import CompartmentalModel


class SIR(CompartmentalModel):
    """SIR Compartmental Model

    TODO : Add docstring

    :parameter region:
        Region for which we are forecasting.

    :parameter disease:
        Accepts

    :parameter method:
        Modeling method. (deterministic, stochastic, hybrid, bayesian)
    """

    def __init__(self,
                 region: Any,
                 disease: Any,
                 method: str = "deterministic",
                 ) -> None:
        self.disease = disease
        self.method = method

    def fit(self, ) -> None:
        pass  # tt
