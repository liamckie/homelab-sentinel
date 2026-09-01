from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    
    
def test_heartbeat():
    response = client.post("/heartbeat")

    assert response.status_code == 200
    assert response.json()["status"] == "received"
    

def test_status_after_heartbeat():
    client.post("/heartbeat")

    response = client.get("/api/status")
    
    print(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "online"            