from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_landing():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"title": "Backend API for the wedding project"}