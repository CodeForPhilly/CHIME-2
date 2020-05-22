# -*- coding: utf-8 -*-
"""
Decorator functions
"""
from functools import wraps

from flask import request

from app.main.route.auth import Auth


def token_required(f):
    """Wraps endpoints that should require authorization"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """checks login status of user"""
        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    """Wraps endpoints that should require admin authorization"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """Validates user status returns 401 if authorization fails"""
        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        admin = token.get("admin")
        if not admin:
            response_object = {"status": "fail", "message": "admin token required"}
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
