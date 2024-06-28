import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:8000"

def test_predict_endpoint(base_url):
    url = f"{base_url}/predict/"
    files = {"file": open("ultralytics/assets/bus.jpg", "rb")}
    data = {
        "classes": ["shoes", "blazer", "jacket", "glasses", "coat"],
        "iou": 0.5,
        "conf": 0.2
    }

    response = requests.post(url, files=files, data=data)
    assert response.status_code == 200
    predictions = response.json()

    # Add assertions for your predictions here
    assert isinstance(predictions, list)
    assert len(predictions) > 0
    # Add more specific assertions as needed

if __name__ == "__main__":
    pytest.main()
