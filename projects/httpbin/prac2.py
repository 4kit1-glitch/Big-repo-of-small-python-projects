import requests
import json

BASE_GET_URL = "https://httpbin.org/get"
BASE_POST_URL = "https://httpbin.org/post"

try:
    response = requests.post(BASE_POST_URL, params= {"name": "kit"}, data={"page": 3}, timeout=3, headers={"X-test": "reacce"})
    response.raise_for_status()

    print(response.text)
except requests.RequestException as err:
    print(f"some error occured: {err}")