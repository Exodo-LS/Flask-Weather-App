# project/tests/context_process_test.py
import datetime
from os import getenv


def test_context_variables_environment(client):
    """This test checks if the environment is printed"""
    response = client.get("/")
    env = getenv('FLASK_ENV', None)
    test_string = f"Environment: {env}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data


def test_context_variables_copyright(client):
    """This tests checks if the copyright is printed"""
    response = client.get("/")
    test_string = f"Copyright: "
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data