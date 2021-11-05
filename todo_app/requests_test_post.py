import requests
from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN

query_params = { "name": "New card for Alex", "idList": "607d77d01a766e323caa0053", "key": TRELLO_KEY, "token": TRELLO_TOKEN}

reqUrl = TRELLO_URL+"/1/cards"

response = requests.post(reqUrl, params=query_params)

print(response.json())