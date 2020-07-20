# -*- coding: utf-8 -*-
"""Defines fixtures available to all test."""

import logging

import pytest
from webtest import TestApp

from src.app import create_app
from src.database import db as _db

from .factories import UserFactory


@pytest.fixture
def app():
    """Create application for the test."""
    _app = create_app("test.settings")
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """Create Webtest app."""
    return TestApp(app)


@pytest.fixture
def db(app):
    """Create database for the test."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """Create user for the test."""
    user = UserFactory(password="myprecious")
    db.session.commit()
    return user
