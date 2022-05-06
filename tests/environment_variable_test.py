# project/tests/environment_variable_test.py
import logging
import os

import app.config


def test_environment_variable_development(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']


def test_environment_variable_testing(application):
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

