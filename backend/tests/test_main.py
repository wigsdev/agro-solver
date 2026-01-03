from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint returns 200 and correct JSON structure.
    """
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Agro-Solver API is running"
    assert "version" in data
