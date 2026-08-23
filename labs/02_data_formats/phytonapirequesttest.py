import requests

url = "https://example.com/api/devices"

headers = {
    "Authorization": "Bearer TOKEN",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()

    for device in devices:
        print(device["hostname"])
else:
    print(f"Request failed: {response.status_code}")