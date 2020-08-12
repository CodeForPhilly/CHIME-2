# -*- coding: utf-8 -*-
"""Type-hinting definitions."""
from typing import TypeVar, Union

# Floats or integers
FloatLike = TypeVar("FloatLike")
# Array of floats or integers
FloatLikeArray = TypeVar("FloatLikeArray")

# Normally distributed random variable
NormalDistVar = TypeVar("NormalDistVar")
# Array of normally distributed random variables
NormalDistArray = TypeVar("NormalDistArray")

ScipyContinuousDistribution = TypeVar("ScipyContinuousDistribution")

FloatOrDistVar = Union[FloatLike, NormalDistVar]
FloatOrDistArray = Union[FloatLikeArray, NormalDistArray]
