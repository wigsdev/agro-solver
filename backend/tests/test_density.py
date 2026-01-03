from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_density_square_system():
    # 2m x 2m Square = 2500
    response = client.post("/api/density", json={
        "row_distance": 2.0,
        "plant_distance": 2.0,
        "system": "square"
    })
    assert response.status_code == 200
    assert response.json()["plants_per_hectare"] == 2500

def test_density_triangular_system():
    # 2m x 2m Triangular = ~2887 (2500 / 0.866)
    response = client.post("/api/density", json={
        "row_distance": 2.0,
        "plant_distance": 2.0,
        "system": "triangular"
    })
    assert response.status_code == 200
    # Allow small rounding differences
    assert 2886 <= response.json()["plants_per_hectare"] <= 2888

def test_density_validation_zero():
    # Zero should fail validation
    response = client.post("/api/density", json={
        "row_distance": 0,
        "plant_distance": 2.0
    })
    assert response.status_code == 422

def test_density_validation_negative():
    # Negative should fail validation
    response = client.post("/api/density", json={
        "row_distance": 2.0,
        "plant_distance": -1.0
    })
    assert response.status_code == 422
