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

import numpy as np

class SIR(CompartmentalModel):
    """SIR Compartmental Model

    """
    def __init__(self):
        pass  ##

    def fit(self, ) -> None:
        """Fit the model to the time series data provided by hospital
        census records"""

    def simulate(self) -> np.array:
        pass  #t

