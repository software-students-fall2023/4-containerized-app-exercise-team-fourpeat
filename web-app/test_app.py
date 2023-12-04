"""Unit tests for the Flask web application."""
import subprocess
import pytest
from app import app
from flask import template_rendered


@pytest.fixture
def client():
    """Client"""
    with app.test_client() as client:
        yield client


def test_animals_db_route(client):
    """Test the animals_db route"""

    # Start recording template rendering signals
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)

    # Perform a GET request to the animals_db route
    with client.get("/") as response:
        pass  # Use the response if needed, for example, response.status_code

    # Disconnect the signal after the request is done
    template_rendered.disconnect(record, app)

    # Verify that the template was rendered with the 'animals' variable
    assert len(recorded) == 1  # Ensure one template was rendered
    template, context = recorded[0]
    assert template.name == "index.html"  # Check the rendered template name
    assert "animals" in context  # Check if 'animals' variable exists in the context


def test_capture_audio_endpoint(client, monkeypatch):
    """Define the data payload to simulate POST request"""
    data = {"word": "dog"}  # Replace with desired data for testing

    # Patch subprocess.run to prevent actual script execution during the test
    # pylint: disable=W0127
    # pylint: disable=R1711
    def mock_subprocess_run(args, check):
        args = args
        check = check
        return None

    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    # Simulate a POST request to the capture_audio endpoint
    response = client.post("/capture_audio", json=data)

    # Assertions
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    assert response.json == {"success": True}  # Check if the response
