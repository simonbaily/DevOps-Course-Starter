import requests
from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN, TODO_APP_BOARD_ID, TO_DO_LIST_ID, DONE_LIST_ID #import secrets for Trello


def get_trello_lists():
    query_params = { "cards": 'open', "key": TRELLO_KEY, "token": TRELLO_TOKEN}
    requrl = f"{TRELLO_URL}/1/boards/{TODO_APP_BOARD_ID}/lists"
    response = requests.get(requrl, params=query_params)
    return (response.json())


def add_card(name):
    """
    Adds a new card on the 'To Do' list to the 'ToDo App using Trello' board in Trello

    Args:
        name: The name of the card. This comes from ndex.html, 

    Returns:
        json object from requests library.
    """
    query_params = { "name": name, "idList": TO_DO_LIST_ID, "key": TRELLO_KEY, "token": TRELLO_TOKEN}
    requrl = f"{TRELLO_URL}/1/cards"
    response = requests.post(requrl, params=query_params)
    return(response.json())


# """
# def get_trello_cards():     #retrieves cards only

#     query_params = { "key": TRELLO_KEY, "token": TRELLO_TOKEN}
#     requrl = f"{TRELLO_URL}/1/boards/{TODO_APP_BOARD_ID}/cards"
#     response = requests.get(requrl, params=query_params)
#     return (response.json())
# """

def update_card(id):
    query_params = { "idList": DONE_LIST_ID, "key": TRELLO_KEY, "token": TRELLO_TOKEN}
    reqUrl = f"{TRELLO_URL}/1/cards/{id}"
    response = requests.put(reqUrl, params=query_params)
    return(response.json())  #not attempted any of this functionality yet
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    # existing_items = get_trello_cards()
    # updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    # session['items'] = updated_items

    # return item
