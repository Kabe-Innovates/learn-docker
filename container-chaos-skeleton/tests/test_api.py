from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    # 1. Send a GET request to "/" (if you have a root endpoint)
    # or just check the health endpoint we made
    response = client.get("/health")
    
    # 2. Assert that the status code is 200 (OK)
    assert response.status_code == 200
    
    # 3. Assert the JSON response matches exactly
    assert response.json() == {"status": "alive"}

def test_prediction_structure():
    # 1. Send fake data to /predict
    payload = {"feature1": 10.5, "feature2": 2.0}
    response = client.post("/predict", json=payload)
    
    # 2. Check if it returns 200
    assert response.status_code == 200
    
    # 3. Check if "prediction" key exists in response
    json_data = response.json()
    assert "prediction" in json_data