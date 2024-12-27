import pytest
from fastapi.testclient import TestClient
from track_app.main import app
from track_app.enums import ChairType  # Only keep if actually needed in tests

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_chair():
    return {
        "groove_width": 2.2,
        "groove_depth": 1.5,
        "fit_adjustment": 0.1,
        "rib_spacing": 1.5,
        "jaw_height": 3.0,
        "placement_offset": 10.0,
        "timber_id": 1,
        "track_id": 1,
        "type": ChairType.S1.value
    }

@pytest.fixture
def sample_timber():
    return {
        "length": 50,
        "width": 10,
        "depth": 5,
        "position": 10.0,
        "track_id": 1
    }

@pytest.fixture
def sample_track():
    return {
        "total_length": 150,
        "timber_spacing": 8.0,
        "chair_alignment": "opposite"
    }

def test_create_chair(client, sample_chair):
    response = client.post("/admin/chairs/", json=sample_chair)
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == ChairType.S1.value
    assert data["groove_width"] == 2.2
    assert data["groove_depth"] == 1.5

def test_read_chairs(client):
    response = client.get("/admin/chairs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_timber(client, sample_timber):
    response = client.post("/admin/timbers/", json=sample_timber)
    assert response.status_code == 201
    data = response.json()
    assert data["length"] == 50
    assert data["width"] == 10

def test_read_timbers(client):
    response = client.get("/admin/timbers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_track(client, sample_track):
    response = client.post("/admin/tracks/", json=sample_track)
    assert response.status_code == 201
    data = response.json()
    assert data["total_length"] == 150
    assert data["timber_spacing"] == 8.0

def test_read_tracks(client):
    response = client.get("/admin/tracks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
