# -*- coding: utf-8 -*-
"""dashboard specific helper functions"""
import os


def load_html(html_file: str):
    """Used to load html file from template dir and pass into homepage
     string"""
    filepath = os.getcwd() + '/app/templates/' + f'{html_file}'
    print(filepath)
    with open(filepath, 'r') as f:
        html_stream = f.read()
    return html_stream


def interpolate_str(template, **data):
    s = template
    for k, v in data.items():
        key = "{%" + k + "%}"
        s = s.replace(key, v)
    return s
