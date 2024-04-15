import requests


Endpoint = "https://todo.pixegami.io/"
response = requests.get(Endpoint)
print (response.json())