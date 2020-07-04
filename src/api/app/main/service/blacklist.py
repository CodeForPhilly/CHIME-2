# -*- coding: utf-8 -*-
"""
Service for blacklisting user tokens
"""
from app.main import db

from app.main.model.blacklist import BlacklistToken


def save_token(token):
    """Save the user token to the blacklist"""
    blacklist_token = BlacklistToken(token=token)
    logout_msg = {"status": "success", "message": "Successfully logged out."}
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = logout_msg
        return response_object, 200
    except Exception as e:
        response_object = {"status": "fail", "message": e}
        return response_object, 200
