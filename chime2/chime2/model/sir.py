# -*- coding: utf-8 -*-
"""SIR compartmental model.

===
SIR
===

TODO: Add background info for SIR model to docstring.
TODO: Implement SIR as a class.
"""
from typing import Set

from model._base import CompartmentalModel

_model_compartments: Set[str] = {'susceptible', 'infected', 'recovered'}
_model_parameters: Set[str] = {}


class SIR(CompartmentalModel):
    """
    =======================
    SIR Compartmental Model
    =======================
    """

    def __init__(self):

        super().__init__(compartments=_model_compartments)

    @property
    def compartments(self):
        return self._compartments

print(SIR().compartments)



