"""parameters/_base.
"""
from collections import namedtuple, OrderedDict
from typing import Any, Callable, List, Dict, NamedTuple, Type, Tuple

param_args = [
    ("key", str),
    ("dtype", Any),
    ("default_value", Any),
    ("distribution", str),
    ("validators", List[Callable]),
    ("description", str),
]

# Holds a single parameter's metadata
RegisteredParameter: NamedTuple[str, Tuple[str, Any]] = NamedTuple(
    "RegisteredParameter", param_args
)

# Stores metadata for all configured parameters
_parameter_registry: Dict[str, RegisteredParameter] = {}
# Reserved keys for special use
_reserved_keys: List[str] = ["all"]
# The temporary holder for key value pair of parameter configuration
_param_config: Dict[str, Any] = {}


class ParameterError(AttributeError, KeyError):  # custom exception
    """
    Error for handling exceptions encountered while interacting with
    parameters.

    Extends on AttributeError, KeyError
    """


def _get_param(pattern: str) -> RegisteredParameter:
    """Attempts to return the registered parameter"""
    p = pattern.lower()
    if p in _parameter_registry:
        return _parameter_registry[p]
    raise ParameterError(f"'{pattern}' is not a parameter")


def _register_param(
    key: str,  # ----------------# parameter 'name'
    dtype: Any,  # --------------# type(<parameter>)
    default_value: Any,  # ------# default value for the parameter if none is found
    distribution: str,  # -------# parameter distribution group
    validators: List[Callable],  # validation functions to be used on the parameter
    description: str = "",  # ---# description of the parameter
) -> None:
    """Attempts to register a parameter"""
    p = key.lower()
    if p in _parameter_registry:
        raise ParameterError(f"'{key}' is already registered!")
    # ensure default value type same as dtype
    if type(dtype) != type(default_value):
        raise ParameterError(f"Default value must be of same type as dtype[{dtype}]")
    # ensure the default value can be validated if validators are included
    if validators:
        for validate in validators:
            validate(default_value)
    if len(description) == 0:
        raise ParameterError("Parameters must include a description")
    # if all checks pass register the parameter with the metadata
    _parameter_registry[p] = RegisteredParameter(
        key=key,
        dtype=dtype,
        default_value=default_value,
        distribution=distribution,
        validators=validators,
        description=description,
    )


def _describe_param(pattern: str) -> str:
    param = _get_param(pattern)
    return param.description


def _get_param_default(pattern: str) -> Any:
    param = _get_param(pattern)
    return param.default_value


def _get_param_type(pattern: str) -> Any:
    """Returns the type of a registered parameter"""
    param = _get_param(pattern.lower())
    return param.dtype


class Parameters:
    """
    Parameters
    ==========

    Holds the current state of all parameters. Reads parameters
    from _param_config and accordingly creates a NamedTuple instance
    which makes all parameters accessible through dot notation.

    """

    _cache: List[Any] = []
    _log_file: str = ""

    _dt_params = ["sim_start", "sim_stop"]
    _epidemiological_params = [
        "recovery_days",
        "initial_doubling_time",
        "hospitalized_rate",
        "icu_rate",
        "vent_rate",
    ]

    def __init__(self, logging: bool = False):
        self.log = logging
        self.__set_parameters__()

    def __reset_parameters__(self):
        """Resets the _param_config registry and wipes own attributes"""
        if hasattr(self, "get"):
            delattr(self, "get")

    def __set_parameters__(self):
        """
        Reads from _param_config and sets parameters accordingly if any
        required parameters are not configured issues warning and reverts
        to default_value from _parameter_registry
        """
        self.__reset_parameters__()

        selected = [(p, _param_config[p]) for p in _param_config.keys()]
        ordered = OrderedDict(selected)

        pars = namedtuple("pars", ordered.keys())

        self.get = pars(**ordered)


def build_dt_series(start_date: str, end_date: str):
    """
    Builds a datetime series
    :param start_date:
    :param end_date:
    :return:
    """
    s = start_date.split("-")
    if (len(s[0]) != 4) or (len(s[1]) + len(s[2]) != 4):
        raise ValueError("Dates must be formatted YYYY-MM-DD")
    e = end_date.split("-")
    if (len(e[0]) != 4) or (len(e[1]) + len(e[2]) != 4):
        raise ValueError("Dates must be formatted YYYY-MM-DD")
    return


class Parameter(object):
    """
    Parameter
    =========

    Base class for all parameters. Parameter subclasses primary purpose
    is to facilitate the decoupling of model and parameter states. Metadata
    reports to the parameter registry upon class definition via
    overriding the __init_subclass__ built-in method. Upon instantiation
    a parameter subclass can then self-validate any arguments passed to
    it during instantiation. Parameter subclasses do not store the current
    parameter state. Instead, this is done by the ChimeParameters object.

    Attributes
    ----------

    - _key {str}:
        parameter name
    - _dtype {Any}:
        type(<PARAMETER>)
    - _default_value {Any}:
        default value to be set when needed (must pass validation)
    _ _distribution {str}:
        ["constant", "beta", "gamma", "normal"]
    - _validators {List[Callable]}:
        list of validation functions which should be run on a parameter
    - _description {str}:
        description of the parameter

    Custom Methods
    --------------

    - __validate__:
        Runs the defined validation functions on a selected parameter
    - __register__:
        Registers the key, value pair (self._key, self._value) with
        _param_config


    Raises
    ------

    - ParameterError:
        Extension of AttributeError and KeyError, thrown when parameter
        already exists, is incorrectly configured or fails to meet another
        criteria.
    """

    _key = None
    _dtype = None
    _default_value = None
    _distribution = None
    _validators = None
    _description = None

    def __new__(cls, *args, **kwargs):
        """Allocator prevents object creation if already registered"""
        if cls._key in _param_config:
            raise ParameterError(f"'{cls._key}' already registered!")
        return super().__new__(cls)

    def __init_subclass__(cls, *args, **kwargs):
        """Registers parameter metadata at subclass definition"""
        _register_param(
            key=cls._key,
            dtype=cls._dtype,
            default_value=cls._default_value,
            distribution=cls._distribution,
            validators=cls._validators,
            description=cls._description,
        )
        return super().__init_subclass__(cls, **kwargs)

    def __setattr__(self, name, value):
        """Raises parameter error if parameter already configured"""
        if self._key in _param_config:
            raise ParameterError("Parameters are immutable!")
        else:
            return super().__setattr__(name, value)

    def __validate__(self, *args, **kwargs):
        """
        Utilizes validators registered at subclass definition to
        validate inputs upon instantiation.
        """
        if "_value" in zip(args, kwargs):
            for v in self._validators:
                v(kwargs["_value"])

    def __describe__(self):
        return self._description
