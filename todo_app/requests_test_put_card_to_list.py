import requests

#this this the next item to do. convert name param to listid to move it from to do to doing/done

from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN, DONE_LIST_ID

query_params = { "idList": DONE_LIST_ID, "key": TRELLO_KEY, "token": TRELLO_TOKEN}

reqUrl = TRELLO_URL+"/1/cards/617152b7b05851899222b9f2"

response = requests.put(reqUrl, params=query_params)

print(response.json())