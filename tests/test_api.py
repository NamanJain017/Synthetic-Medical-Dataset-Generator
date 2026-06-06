from fastapi.testclient import TestClient
from src.interface.api import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert "gpu_available" in response.json()
