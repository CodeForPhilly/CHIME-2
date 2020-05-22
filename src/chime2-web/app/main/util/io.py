# -*- coding: utf-8 -*-
"""
I/O helper functions
--------------------

Helper functions for file I/O and read / write operations.

Contains
~~~~~~~~

-
"""
from os import path
from typing import Any, Dict, Optional
from yaml import safe_load

from app.main import config


def get_localization_file(localization_file: str) -> str:
    """Returns the path to the localization file"""
    return path.join(config.locale_path, config.language, localization_file)


def read_localization_yml(file: str) -> Dict[str, Any]:
    """Reads localization template. Localization determined from
    configuration settings.

    :parameter file:
            Name of the section plus `.md`

    :raises KeyError:
        If no template for file/language exists.
    """
    filepath = get_localization_file(localization_file=file)
    if not path.exists(filepath):
        raise KeyError(
            f"No template found for "
            f"language '{config.language}' and "
            f"section '{file}'"
        )
    with open(filepath) as f:
        yaml = safe_load(f)
    return yaml


def read_localization_markdown(file: str) -> str:
    """Reads localization template. Language set via configuration
     settings.

    :param file:
        Name of the section plus ``.md``

    :raises KeyError:
        If no template for file/language exists.
    """
    filepath = get_localization_file(localization_file=file)
    if not path.exists(filepath):
        raise KeyError(
            "No template found for "
            f"language '{config.language}' and "
            f"section '{file}'"
        )
    with open(filepath) as f:
        md = f.read()
    return md
