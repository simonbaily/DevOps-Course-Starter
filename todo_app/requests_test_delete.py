import requests
from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN

query_params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}

reqUrl = TRELLO_URL+"/1/cards/61461b433055f388b9387a65"

response = requests.delete(reqUrl, params=query_params)

print(response.json())