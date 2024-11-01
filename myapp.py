# example application to communicate with api


import requests # type: ignore
import json
URL = "http://127.0.0.1:8000/stucreate/"

data={
    'name':'Sonam',
    'roll': 101,
    'city':'Ranchi'
}
json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)


def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
get_data(1)   
