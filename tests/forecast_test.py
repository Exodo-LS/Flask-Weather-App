# project/tests/simple_pages_test.py
from app.db.models import User
"""This tests the forecast pages"""


def test_forecast_page_exists(client):
    """This validates the forecast page"""
    response = client.get("/temperature_forecast")
    assert response.status_code == 405

