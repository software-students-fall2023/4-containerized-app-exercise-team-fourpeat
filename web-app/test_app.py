"""Unit tests for the Flask web application."""
import pytest
from app import app
import subprocess


@pytest.fixture
def client():
    """Client"""
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Animal Sounds" in response.data


def test_capture_audio_endpoint(client, monkeypatch):
    # Define the data payload to simulate POST request
    data = {"word": "dog"}  # Replace with desired data for testing

    # Patch subprocess.run to prevent actual script execution during the test
    def mock_subprocess_run(args, check):
        return None

    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # Simulate a POST request to the capture_audio endpoint
    response = client.post("/capture_audio", json=data)

    # Assertions
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert response.json == {"success": True}  # Check if the response
