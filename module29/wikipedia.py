import requests
url = "https://en.wikipedia.org"

try:
    response = requests.get(url)
    response.raise_for_status()
    print("response.text")
except requests.exceptions.RequestException as req_err:
