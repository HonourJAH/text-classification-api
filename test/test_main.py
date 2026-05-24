from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}


def test_predict_success():
    payload = {
        "text": "Artificial intelligence is transforming modern software systems."
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert "predicted_category" in data
    assert isinstance(data["predicted_category"], str)


def test_predict_validation_error_short_text():
    payload = {"text": "Too short"}

    response = client.post("/predict", json=payload)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_predict_missing_text_field():
    payload = {}

    response = client.post("/predict", json=payload)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
