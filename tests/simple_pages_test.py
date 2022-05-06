# project/tests/simple_pages_test.py
"""This test the homepage"""


def test_nav_bar_simple_pages_links(client):
    """This This tests to see if the Simple Page templates are in the nav bar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data


def test_index_page_exists(client):
    """This validates the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_about_page_exists(client):
    """This validates the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_welcome_page_exists(client):
    """This validates the welcome page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"welcome" in response.data

