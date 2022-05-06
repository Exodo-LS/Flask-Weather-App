# project/tests/environment_variable_test.py
import logging
import os

import app.config


def test_environment_variable_development(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']

