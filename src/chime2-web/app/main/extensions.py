# -*- coding: utf-8 -*-
"""
Flask extension loading
"""
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

manager = Manager()
db = SQLAlchemy()
encrypt = Bcrypt()
