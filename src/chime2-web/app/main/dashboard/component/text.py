# -*- coding: utf-8 -*-
"""
Text components
"""
from typing import Any, Dict, List

import dash_core_components as dcc
import dash_html_components as html
from dash.development.base_component import ComponentMeta

from .base import Component
from app.main.util.io import read_localization_markdown, read_localization_yml

_valid_extensions = ["md", "yaml", "yml"]


def _get_file_extension(localization_file: str) -> str:
    """Parse the file extension from a given file"""
    return localization_file.split(".")[-1]


def _validate_file(pattern: str) -> None:
    """Verify supplied file extension is one of valid extensions"""
    if _get_file_extension(pattern).lower() not in _valid_extensions:
        msg = f"'{pattern}' is not an accepted format"
        raise ValueError(msg)


def _infer_file_read(localization_file: str) -> Any:
    """Use the correct file load utility based on file extensions.
    Assumes file extension has previously been validated."""
    ext = _get_file_extension(localization_file)
    return (
        (read_localization_yml(localization_file))
        if ext in ["yaml", "yml"]
        else read_localization_markdown(localization_file)
    )


class Text(Component):
    """Class for static text sections (eg. paragraphs).

    :argument localization_file: str
        localization file to load for text section
    """

    def __init__(self, localization_file: str):
        super().__init__()
        _validate_file(localization_file)
        self._file = localization_file

    def _load_file(self):
        """Loads the localization file and stores output in
         self._content."""
        self._content = _infer_file_read(self._file)

    def _get_html(self, _html: List[ComponentMeta]) -> List[ComponentMeta]:
        """Defines _html as the output of _load_file method"""
        return html.Div([dcc.Markdown(self._content)])
