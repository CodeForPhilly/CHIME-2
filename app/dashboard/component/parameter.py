# -*- coding: utf-8 -*-
"""Parameter Input Component."""
import re
from typing import Dict

import dash_core_components as dcc
import dash_html_components as html

from app.dashboard._config import PARAMETER_META


def _interpolate_component_type(parameter_type: str) -> str:
    """Return appropriate component type for parameter data type."""
    if parameter_type in ['int', 'float']:
        return "number"


def _build_component(meta):
    """Build the input component from configuration file data.

    :return: dash_bootstrap_components.InputGroup
    """
    title = meta['title']
    label = meta['label']
    component_id = meta['param_key']
    component_type = _interpolate_component_type(meta['dataType'])

    return html.Div(className="form-group",
                    children=[
                        html.Label(f'{label}',
                                   title=title,
                                   htmlFor=f'{component_id}'
                                   ),
                        dcc.Input(className='form-control',
                                  type=component_type,
                                  id=f'{component_id}'
                                  )
                    ])


class ParameterInput(object):
    """Input component group for individual parameters."""

    def __init__(self, component_meta):
        """

        :param component_meta:
        """
        print(component_meta)
        self._component = _build_component(meta=component_meta)

    @property
    def component(self):
        return self._component


class ParameterGroup(object):
    """Associated group of parameter input components."""

    def __init__(self, parameter_group: Dict[str, str]) -> None:

        self._label = html.Div(className='card-header',
                               style={'textAlign': 'center'},
                               children=[
                                   html.H5(f'{parameter_group["groupLabel"]}',
                                           className="display-5",
                                           style={'fontWeight': 'bold'}
                                           )])
        self._component_group = []

        for key, meta in parameter_group.items():
            if key != 'groupLabel':
                self._component_group.append(_build_component(meta=meta))

    @property
    def container(self):
        return html.Div(className='card',
                        children=[
                            self._label,
                            html.Div(className='card-body',
                                     children=self._component_group),
                            html.Div(className='card-footer')
                        ])


def build_parameter_inputs():
    component_groups = {}
    for meta in PARAMETER_META.values():
        group_key = re.sub(r' ', r'-', meta['groupLabel']).lower()
        component_groups[f'{group_key}'] = ParameterGroup(parameter_group=meta)

    return component_groups
