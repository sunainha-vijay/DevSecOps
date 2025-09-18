import json
from challenge3.app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_addition():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json["result"] == 8

def test_divide_by_zero():
    client = app.test_client()
    response = client.post("/calculate", json={"operation": "divide", "a": 5, "b": 0})
    assert response.status_code == 400
    assert "error" in response.json

