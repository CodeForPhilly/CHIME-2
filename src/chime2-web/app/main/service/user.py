# -*- coding: utf-8 -*-
"""
User functions
"""
import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    """
    Check if database already contains an entry for the user email. If
    not then register new user to database.

    - public_id {str} uuid (primary key) \n
    - email {str} -- user.email \n
    - username {str} -- user.name \n
    - password {str} -- user.password \n
    - registered_on {int} -- datetime.datetime.utcnow()

    :param data:
        user registration data
    :return:
        SUCCESS [auth token] FAIL [409, fail message]
    """
    user = User.query.filter_by(email=data["email"]).first()
    new_user = User(
        public_id=str(uuid.uuid4()),
        email=data["email"],
        username=data["username"],
        password=data["password"],
        registered_on=datetime.datetime.utcnow(),
    )

    if not user:
        save_changes(new_user)
        return generate_token(new_user)

    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    """Returns all registered users"""
    return User.query.all()


def get_a_user(public_id):
    """Returns user info from public id"""
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    """Generate a new authentication token.

    :param user:
        user object

    :return:
        SUCCESS: Auth token FAIL: 201, Exception data
    """
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            "status": "success",
            "message": "Successfully registered.",
            "Authorization": auth_token.decode(),
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return response_object, 401


def save_changes(data):
    """Commit changes to database."""
    db.session.add(data)
    db.session.commit()
