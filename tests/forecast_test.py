# project/tests/forecast_test.py
from app.db.models import User
"""This tests the forecast pages"""


def test_forecast_page_exists(client):
    """This validates the forecast page"""
    response = client.get("/temperature_forecast")
    assert response.status_code == 302


def test_forecast_page_access(client):
    """This validates access to the forecast page"""
    response = client.get("/temperature_forecast")
    test_user = 'IS219_TestUser@email.com'
    test_password = 'Dummy_Pass_123'
    if User.email == test_user and User.password == test_password:
        if User.authenticated:
            assert 'User Authenticated' in response.data
    elif not User.authenticated:
        assert 'User Not Authenticated' in response.data
