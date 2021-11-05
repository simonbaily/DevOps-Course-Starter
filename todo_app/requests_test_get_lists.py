import requests
from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN, TODO_APP_BOARD_ID

query_params = { "cards": 'all', "key": TRELLO_KEY, "token": TRELLO_TOKEN}

requrl = f"{TRELLO_URL}/1/boards/{TODO_APP_BOARD_ID}/lists"

response = requests.get(requrl, params=query_params)

print(response.json())


