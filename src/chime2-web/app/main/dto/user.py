# -*- coding: utf-8 -*-
"""
User DTOs
---------

:class UserDto:
    User data transfer object, contains available user data.

:class AuthDto
    Contains information needed for login
"""
from flask_restx import Namespace, fields


class UserDto:
    """
    =======
    UserDto
    =======

    Data transfer object for user related operations

    ---

    namespace: ``user``

    ---

    email - string \n
    username - string \n
    password - string \n
    public_id - string
    """

    api = Namespace("user", description="")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "password": fields.String(required=True, description="user password"),
            "public_id": fields.String(description="user Identifier"),
        },
    )


class AuthDto:
    """
    =======
    AuthDto
    =======

    Data transfer object for user related operations

    ---

    namespace: ``auth``

    ---

    email - string \n
    username - string \n
    password - string \n
    public_id - string
    """

    api = Namespace("auth", description="login/logout operations")
    user_auth = api.model(
        "auth_details",
        {
            "email": fields.String(required=True, description="The email address"),
            "password": fields.String(required=True, description="The user password "),
        },
    )
