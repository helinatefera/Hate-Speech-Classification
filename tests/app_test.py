import pytest
from flask import Flask
from app.main_app import app 

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hate Speech Classifier" in response.data

def test_api_get_prediction(client):
    response = client.get("/api/predict?text=I%20love%20you")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "prediction" in json_data
    assert "confidence" in json_data

def test_api_post_prediction(client):
    response = client.post("/api/predict", json={"text": "I hate you"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "prediction" in json_data
    assert "confidence" in json_data
