import time

import requests

while True:
    for station in ["STACJA001", "STACJA002", "STACJA003"]:
        data = requests.get(f"http://127.0.0.1:8000/weather/{station}")
        print(data.json())

    time.sleep(10)