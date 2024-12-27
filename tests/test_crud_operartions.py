import pytest
from fastapi.testclient import TestClient
from main import app  # Ensure the app is properly imported

client = TestClient(app)

@pytest.fixture
def sample_chair():
    return {
        "slot_depth": 0.8,
        "slot_width": 0.5,
        "tolerance": 0.02
    }

@pytest.fixture
def sample_timber():
    return {
        "position": 10.0,
        "width": 5.0,
        "thickness": 2.5,
        "material": "wood"
    }

@pytest.fixture
def sample_track():
    return {
        "length": 100.0,
        "chair_spacing": 12.0,
        "sleeper_spacing": 10.0
    }

def test_create_chair(sample_chair):
    response = client.post("/admin/chairs/", json=sample_chair)
    assert response.status_code == 200
    data = response.json()
    assert data["slot_depth"] == sample_chair["slot_depth"]
    assert data["slot_width"] == sample_chair["slot_width"]
    assert data["tolerance"] == sample_chair["tolerance"]

def test_read_chairs():
    response = client.get("/admin/chairs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_timber(sample_timber):
    response = client.post("/admin/timbers/", json=sample_timber)
    assert response.status_code == 200
    data = response.json()
    assert data["position"] == sample_timber["position"]
    assert data["width"] == sample_timber["width"]
    assert data["thickness"] == sample_timber["thickness"]

def test_read_timbers():
    response = client.get("/admin/timbers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_track(sample_track):
    response = client.post("/admin/tracks/", json=sample_track)
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == sample_track["length"]
    assert data["chair_spacing"] == sample_track["chair_spacing"]
    assert data["sleeper_spacing"] == sample_track["sleeper_spacing"]

def test_read_tracks():
    response = client.get("/admin/tracks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_chair():
    # Create a chair to delete
    response = client.post("/admin/chairs/", json={"slot_depth": 1.0, "slot_width": 0.6, "tolerance": 0.05})
    chair_id = response.json()["id"]

    # Delete the chair
    delete_response = client.delete(f"/admin/chairs/{chair_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Deleted successfully"

def test_delete_timber():
    # Create a timber to delete
    response = client.post("/admin/timbers/", json={"position": 15.0, "width": 6.0, "thickness": 3.0, "material": "plastic"})
    timber_id = response.json()["id"]

    # Delete the timber
    delete_response = client.delete(f"/admin/timbers/{timber_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Deleted successfully"

def test_delete_track():
    # Create a track to delete
    response = client.post("/admin/tracks/", json={"length": 120.0, "chair_spacing": 14.0, "sleeper_spacing": 12.0})
    track_id = response.json()["id"]

    # Delete the track
    delete_response = client.delete(f"/admin/tracks/{track_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Deleted successfully"
