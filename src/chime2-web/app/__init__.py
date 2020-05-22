# -*- coding: utf-8 -*-
"""
====
Main
====

"""

from flask_restx import Api
from flask import Blueprint

from .main.route.user import api as user_ns
from .main.route.auth import api as auth_ns

# from .main.route.chime import api as chime_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Covid-19 Hospital Impact Model for Epidemics",
    version="2.0",
    description="",
)

api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns)
