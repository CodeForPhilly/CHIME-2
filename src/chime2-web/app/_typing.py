"""app/_typing.py

_typing
#######

Custom types and imported types for use in the app
"""
from pathlib import Path
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    AnyStr,
    Callable,
    Collection,
    Dict,
    Hashable,
    List,
    Mapping,
    Optional,
    Type,
    TypeVar,
    Union,
)

# Place internal imports in the branch with forward ref "# noqa: F401"
if TYPE_CHECKING:
    from chime2.app.dashboard import Dashboard  # noqa: F401
