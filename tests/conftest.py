# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from track_app.main import app  # or wherever your FastAPI app is defined

@pytest.fixture(scope="session")
def client():
    """Create a TestClient for our FastAPI app."""
    return TestClient(app)
