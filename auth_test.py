from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_success():
    form_data = {"username": "user1", "password": "password1"}
    response = client.post("/token", data=form_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_failure():
    form_data = {"username": "invalid_user", "password": "invalid_password"}
    response = client.post("/token", data=form_data)
    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"] == "Bearer"
    assert response.json()["detail"] == "Incorrect username or password"
