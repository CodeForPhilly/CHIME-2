# -*- coding: utf-8 -*-
"""components/navbar
Navigation bar view
"""
from typing import List

import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.development.base_component import ComponentMeta

from .base import Component
from app.main import config

_menu_settings = config.menu_config

_brand_text = "COVID-19 Hospital Impact Model for Epidemics (CHIME-2)"

class Menu(Component):
    """Drop down menu built from configuration settings."""

    def get_html(self) -> List[ComponentMeta]:
        """Define the menu layout"""
        menu = dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(_menu_settings["header"], header=True),
                dbc.DropdownMenuItem(
                    _menu_settings["item-0"][0],
                    _menu_settings["item-0"][1],
                    external_link=True,
                    target="_blank",
                ),
                dbc.DropdownMenuItem(
                    _menu_settings["item-1"][0],
                    _menu_settings["item-1"][1],
                    external_link=True,
                    target="_blank",
                ),
            ],
            in_navbar=True,
            label="Learn More",
            color="light",
            right=True,
        )
        return [menu]


class Navbar(Component):
    """Navigation bar contains menu and brand"""
    menu = Menu()

    def __init__(self):
        super().__init__()

    def get_html(self) -> List[ComponentMeta]:
        """Initialize the navigation bar"""
        nav = dbc.Navbar(
            className="penn-medicine-header px-0",
            children=html.Div(
                className="d-flex align-items-center w-100",
                children=[
                    html.Div(
                        className="px-3",
                        style={"width": "320px"},
                        children=html.A(
                            href="https://www.pennmedicine.org",
                            className="penn-medicine-header__logo",
                            title="Go to the Penn Medicine home page",
                        ),
                    ),
                    html.Div(
                        className="flex-fill",
                        children=dbc.Container(
                            children=[
                                dbc.NavbarBrand(
                                    children=html.H1(
                                        style={"font": "inherit", "margin": "0"},
                                        children=_brand_text,
                                    ),
                                    href="/",
                                )
                            ]
                            + self.menu.component
                        ),
                    ),
                ],
            ),
            dark=True,
            fixed="top",
            color="",
        )
        return [nav]
