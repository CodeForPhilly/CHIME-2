# -*- coding: utf-8 -*-
"""Base class for compartmental models."""
from typing import Any, Dict, List

from chime2.util.timeseries import DatetimeArray


class CompartmentalModel(object):

    _model_params: List[str] = ['dates']
    _alternate_params: List[str] = list()
    _compartments: List[str] = list()

    @classmethod
    def _validate_model_parameters(cls,
                                   model_parameters: Dict[str, Any]) -> None:
        """Validate model parameters pre-fitting."""

        dates = DatetimeArray(model_parameters['dates'])
