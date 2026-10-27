# sends a get request to httpbin to simulate a reaponse

import requests
import json

BASE_GET_URL = "https://httpbin.org/get"
BASE_POST_URL = "https://httpbin.org/post"

try:
    response = requests.get(BASE_GET_URL, params={"page": "tom & jerry"}, timeout=3)
    response.raise_for_status()

    print(response.text)
except requests.RequestException as err:
    print(f"some error occured: {err}")