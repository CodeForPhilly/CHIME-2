# -*- coding: utf-8 -*-
""".. currentmodule:: app:

Configuration files
-------------------
"""
from os import environ, path
from pathlib import Path
from typing import List, Dict, Any, MutableMapping

import toml
from dotenv import load_dotenv
import dash_bootstrap_components as dbc

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


def _get_conf(pattern: str) -> MutableMapping[str, Any]:
    """Get the toml configuration file"""
    return toml.load("etc/" + pattern.lower() + ".toml")


def _abs_path(filepath: str) -> str:
    return str(Path(filepath).absolute())


_app_config = _get_conf("app")["chime2"]
_user_config = _get_conf("user")


class ConfigurationError(AttributeError, KeyError):
    """Exception class for configurations and settings"""


class Config:
    """Configuration settings and environment variables"""

    # ==========================
    # Application configurations
    # ==========================
    # ---------------
    # path references
    # ---------------
    locale_path = _abs_path(_app_config["localization"]["path"])
    assets_path = _abs_path(_app_config["assets"]["path"])
    _src_root = _abs_path("chime2-web")
    # -------------------
    # user configurations
    # -------------------
    language = _user_config["language"]
    # ------------------------
    # dashboard configurations
    # ------------------------
    dashboard_route = _app_config["dashboard"]["route"]
    dashboard_title = _app_config["dashboard"]["title"]
    dash_stylesheets = [dbc.themes.BOOTSTRAP] + list(
        _app_config["dashboard"]["stylesheets"].values()
    )
    dash_scripts: List[str] = []
    menu_config = _app_config["dashboard"]["menu"]
    # --------------------
    # Flask configurations
    # --------------------
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    DEBUG = False


class Development(Config):
    """Development configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "chime.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    """Testing configuration"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "chime.db")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """Production Configuration"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "chime.db")
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # postgres
    # SQLALCHEMY_DATABASE_URI = <>


def config_from_object(context: str = "prod"):
    """
    One of ['dev', 'test', 'prod']. Returns configuration object
    based on selected context.
    :param context:
        Environment context either 'dev', 'test', or 'prod'.
    :return:
        Configuration object.
    """
    configs = {"dev": Development(), "test": Testing(), "prod": Production()}
    if context.lower() not in configs:
        raise ConfigurationError(f"'{context}' not a valid context")
    return configs[context.lower()]


key = Config.SECRET_KEY
