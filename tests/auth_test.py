# project/tests/auth_test.py
import pytest
from app.db.models import User


def test_nav_bar_authentication_links(client):
    """This tests to see if the Auth Pages are in the nav bar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
