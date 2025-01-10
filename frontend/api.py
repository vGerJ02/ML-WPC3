import requests

def submit_data(payload):
    try:
        response = requests.post("http://localhost:8000/submit/", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(e)
        return None
