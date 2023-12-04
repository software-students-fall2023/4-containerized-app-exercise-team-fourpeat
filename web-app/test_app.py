"""Unit tests for the Flask web application."""
import subprocess
import pytest
from app import app


@pytest.fixture
def client():
    """Client"""
    with app.test_client() as client:
        yield client


def test_capture_audio_endpoint(client, monkeypatch):
    """Test the capture_audio endpoint"""

    # Define the data payload to simulate a POST request
    data = {"word": "dog"}  # Replace with desired data for testing

    # Patch subprocess.run to prevent actual script execution during the test
    mock_subprocess_run = lambda *args, **kwargs: None

    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # Simulate a POST request to the capture_audio endpoint
    response = client.post("/capture_audio", json=data)

    # Assertions
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert response.json == {
        "success": True
    }  # Check if the response JSON matches the expected result
