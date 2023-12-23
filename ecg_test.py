from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# TODO: WIP
def test_upload_ecg(mocker):
    mocker.patch("app.application.auth_user.authenticate_user", return_value={"username": "user1", "role": "USER"})
    ecg_data = {
        "id": 0,
        "date": "string",
        "leads": [
            {
                "name": "string",
                "number_of_samples": 0,
                "signal": [
                    0
                ]
            }
        ]
    }

    response = client.post("/upload_ecg/", json=ecg_data)
    assert response.status_code == 200
    assert response.json() == ecg_data


# def test_get_ecg_insights_by_ecg_id(mocker):
#     # mocker.patch("app.application.auth_user.authenticate_user", return_value={"username": "test_user", "role": "USER"})
#     ecg_id = 1
#     response = client.get(f"/get_ecg_insights_by_ecg_id/{ecg_id}")
#     assert response.status_code == 200
#     # assert "key" in response.json()
#     # assert response.json()["key"] == "value"


# def test_get_ecg_insights_by_ecg_id_not_found(mocker):
#     # mocker.patch("app.application.auth_user.authenticate_user", return_value={"username": "test_user", "role": "USER"})
#     ecg_id = 9999
#     response = client.get(f"/get_ecg_insights_by_ecg_id/{ecg_id}")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "ECG not found"
