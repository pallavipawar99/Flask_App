import requests

def test_api():
    url = "http://127.0.0.1:5000/process"
    payload = {"name": "Developer"}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Test Passed!")
            print("Response:", response.json())
        else:
            print(f"Test Failed with status: {response.status_code}")
    except Exception as e:
        print(f"Could not connect to server: {e}")

if __name__ == "__main__":
    test_api()
