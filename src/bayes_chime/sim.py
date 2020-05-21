"""

==========
Simulation
==========

TODO : Document

"""
import datetime as dt

from .model.base import ModelError
from .model.sir import SIR
from .model.seir import SEIR

import numpy as np


def _build_dt_index(parameters: Dict[str]) -> np.ndarray:
    """
    Builds an index from a start date and stop date
    :param start:
        Starting date.
    :param stop:
        Ending date.
    :return:
        Datetime index as a numpy n dimensional array.
    """
    start = parameters["start_date"]
    stop = parameters["stop_date"]

    if start > stop:
        raise ModelError("Start date must be before stop date")
    dt_len = abs((start - stop).days)
    return np.arange(dt_len, dtype=np.int16)


class BayesianCHIME(object):
    """Many factors surrounding the transmission, severity of
    infections, and remaining susceptibility of local populations
    to COVID-19 remain highly uncertain. However, as new data on
    hospitalized cases becomes available, we wish to incorporate this
    data in order to update and refine our projections of future demand
    to better inform capacity planners. To that end we have extended
    CHIME to increase the epidemiological process realism and to
    coherently incorporate new data as it becomes available. This
    extension allows us to transition from a few scenarios
    to assess best and worst case projections based on parameter
    assumptions, to a probabilistic forecast representing a continuous
    distribution of likely scenarios.
    """

    # def __init__(
    #     self,
    #     model: str = "SIR",
    #     # Setting to true enforces the normal extension
    #     distributions: str = "normal",
    #     #
    # ) -> None:

