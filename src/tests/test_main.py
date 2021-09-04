from starlette.testclient import TestClient

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_landing(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"title": "Backend API for the wedding project"}

# def test_login():
#     response = cliend.post("/login")
#     assert response.status_code == 200
    # assert response.json() == 