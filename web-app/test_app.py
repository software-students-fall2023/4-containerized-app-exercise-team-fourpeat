"""Unit tests for the Flask web application."""
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Animal Sounds" in response.data

def test_run_route(client):
    """Test the /run route."""
    response = client.get("/run")
    assert response.status_code == 302
