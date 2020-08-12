"""Utilities for the normal CHIME Bayes module
"""
from numpy import exp

from ._typing import FloatOrDistArray, FloatOrDistVar


def logistic_fcn(x: FloatOrDistArray,  # pylint: disable=C0103
                 L: FloatOrDistVar,
                 k: FloatOrDistVar,
                 x0: FloatOrDistVar,
                 ) -> FloatOrDistArray:
    """Compute ``L / (1 + exp(-k(x-x0)))``."""
    return L / (1 + exp(-k * (x - x0)))


def one_minus_logistic_fcn(x: FloatOrDistArray,  # pylint: disable=C0103
                           L: FloatOrDistVar,
                           k: FloatOrDistVar,
                           x0: FloatOrDistVar,
                           ) -> FloatOrDistArray:
    """Compute ``1 - L / (1 + exp(-k(x-x0)))``."""
    return 1 - logistic_fcn(x, L, k, x0)
