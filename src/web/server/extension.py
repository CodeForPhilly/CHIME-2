from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def register_extensions(server):
    db.init_app(server)
    login.init_app(server)
    login.login_view = "main.login"
    migrate.init_app(server, db)
