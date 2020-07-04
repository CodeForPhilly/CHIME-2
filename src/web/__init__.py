from flask import Flask

from config import BaseConfig
from app.server import register_blueprints
from app.server.extension import register_extensions
from .dashboard import register_dashboard


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashboard(server)
    register_extensions(server)
    register_blueprints(server)

    return server
