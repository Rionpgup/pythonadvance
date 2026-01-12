import requests
 url =

 response = requests.get(url)

 if response.status_code != 200:
     print("response.text")
 else:
     print(f"failed to retrieve the webpage; Status code {url}")