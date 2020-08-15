# -*- coding: utf-8 -*-
"""Main library interface.
"""
from collections import namedtuple
from typing import List, Dict, Tuple

_valid_parameters: List[str] = []
_extensions: List[str] = ['normal']
_models: List[str] = ['SIR', 'SEIR']


def _callable_value_error(setting: str,
                          user_choice: str,
                          legal_choices: List[str]
                          ) -> str:
    message = f"'{user_choice}' not implemented for {setting} argument," + \
              "try one of these instead:" + \
              f"\n{' '.join(legal_choices)}"
    return message


class CHIME2(object):
    """Class representation of CHIME 2 from Penn Medicine."""

    def __init__(self,
                 extension: str = 'normal',
                 model: str = 'SEIR'
                 ) -> None:

        if model not in _models:
            raise ValueError(_callable_value_error(setting='model',
                                                   user_choice=model,
                                                   legal_choices=_models
                                                   )
                             )
        if model == 'SIR':
            from chime2.models import SIRModel
            self._model = SIRModel()
        elif model == 'SEIR':
            from chime2.models import SEIRModel
            self._model = SEIRModel()

        if extension not in _extensions:
            raise ValueError(_callable_value_error(user_choice=extension,
                                                   legal_choices=_extensions,
                                                   setting='extension'
                                                   )
                             )
        self._mode = extension

    def fit(self):
        """Fit the simulation to the provided data."""

    def simulate(self):
        """Execute the simulation."""

    def plot(self):
        """Return plots."""
