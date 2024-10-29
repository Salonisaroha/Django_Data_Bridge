# example application to communicate with api


import requests # type: ignore
URL = "http://127.0.0.1:8000/stuinfo/1"

r = requests.get(url = URL)

data = r.json()
print(data)