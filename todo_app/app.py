from flask import Flask, render_template, redirect, request # used for jinja and getting post requests
from todo_app.trello_config import TRELLO_URL, TRELLO_KEY, TRELLO_TOKEN, TRELLO_USERNAME #import secrets for Trello

from todo_app.flask_config import Config 

from todo_app.data.session_items import * # can use * as a wildcard to take everything from another file

app = Flask(__name__)
app.config.from_object(Config)

#display index.html template with list of items via get_items function
@app.route('/', methods=['GET'])
def index():
    items = get_items()
    return render_template('index.html', items=items)

#Capture form post from /newitem form action in index.html
@app.route('/newitem', methods=['POST'])
def addNewItem():
    newItem = request.form['createNew']
    add_item(title = newItem)
    return redirect('/')
      

if __name__ == '__main__':
    app.run()
