import json
from app import app

def test_health():
    """
    Tests the /health endpoint to ensure it's running and returns a success status.
    This is a basic check to confirm the API is responsive.
    """
    # Arrange: Set up the test client
    client = app.test_client()

    # Act: Send a GET request to the /health endpoint
    response = client.get("/health")

    # Assert: Check for a successful status code and the correct JSON response
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_addition():
    """
    Tests a valid addition operation via the /calculate endpoint.
    """
    # Arrange: Set up the test client
    client = app.test_client()

    # Act: Send a POST request with JSON data for an addition calculation
    response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})

    # Assert: Check for a successful status code and that the result is correct
    assert response.status_code == 200
    assert response.json["result"] == 8

def test_divide_by_zero():
    """
    Tests the
