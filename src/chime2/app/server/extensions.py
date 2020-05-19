from flask_jwt import JWT
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


jwt = JWT()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
