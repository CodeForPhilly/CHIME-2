from flask import Blueprint

bp = Blueprint("main", __name__)


def register_blueprints(server):
    from app.server.webapp import server_bp

    server.register_blueprint(server_bp)
