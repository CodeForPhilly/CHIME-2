# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import json

from flask import flash


def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)


def load_html(html_file: str):
    """Used to load html file from template dir and pass into homepage string."""
    with open(html_file, "r") as f:
        html_stream = f.read()
    return html_stream


def load_json(json_file: str):
    """Load json file."""
    with open(json_file, "r") as f:
        contents = json.load(f)
    return contents


def interpolate_str(template, **data):
    """Parse and fill values in custom index string."""
    s = template
    for k, v in data.items():
        key = "{%" + k + "%}"
        s = s.replace(key, v)
    return s
