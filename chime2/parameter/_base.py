"""
Model parameter base class
"""
from collections import namedtuple
from typing import Any, Callable, Dict, List, Union

parameter_attrs = ['param_key',
                   'data_type',
                   'default_val',
                   'description',
                   'distribution',
                   'validators',
                   ]

ModelParameter = namedtuple("ModelParameter", parameter_attrs)

_parameter_registry: Dict[str, ModelParameter] = {}
_valid_distributions: List[str] = ["constant", "beta", "gamma"]


class ParameterError(AttributeError, KeyError):
    """Exception for model parameters"""


def _get_parameter(pattern: str):
    """Return a parameter from the registry"""
    p = pattern.lower()
    if p not in _parameter_registry:
        raise ParameterError(f"'{pattern}' not a registered parameter.")
    return _parameter_registry[p]


def _register_parameter(param_key: str,
                        data_type: type,
                        default_val: Union[int, float],
                        description: str,
                        distribution: str,
                        validators: List[Callable]
                        ):
    if _get_parameter(param_key):  # Check parameter not already registered
        raise ParameterError(f"'{param_key}' already registered.")
    # Avoid potential for NameError by forcing to lower
    key = param_key.lower()
    # Verify default value is of correct type
    if type(default_val) != type(data_type):
        raise ParameterError(f"Invalid data type for parameter '{param_key}'")
    # Ensure a valid distribution is set for the parameter
    if distribution not in _valid_distributions:
        raise ParameterError(
            f"Invalid distribution for '{param_key}' "
            f"must be one of {_valid_distributions}"
        )
    # Verify that a description accompanies the parameter
    if not description:
        raise ParameterError(f"No valid description for '{param_key}'")
    if validators:  # Ensure the default value can pass validation checks
        for v in validators:
            v(default_val)
    # Register parameter if all checks pass
    _parameter_registry[key] = ModelParameter(param_key=key,
                                              data_type=data_type,
                                              default_val=default_val,
                                              description=description,
                                              distribution=distribution,
                                              validators=validators
                                              )
