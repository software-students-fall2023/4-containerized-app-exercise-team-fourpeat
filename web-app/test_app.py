"""Unit tests for the Flask web application."""
import pytest
from app import app


@pytest.fixture
def client():
    """Client"""
    with app.test_client() as client:
        yield client
