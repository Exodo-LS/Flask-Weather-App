"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
# project/tests/conftest.py
import os

import pytest
from app import create_app, User
from app.db import db


# this is a good tutorial I used to fix this code to do datbase testing.
# https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/

@pytest.fixture()
def application():
    """This makes the app"""
    # you need this one if you want to see whats in the database
    # os.environ['FLASK_ENV'] = 'development'
    # you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        # drops the database tables after the test runs
        db.drop_all()


@pytest.fixture()
def test_add_user(application):
    """This tests the add user to database"""
    with application.app_context():
        # new record
        user = User('test_user@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()
