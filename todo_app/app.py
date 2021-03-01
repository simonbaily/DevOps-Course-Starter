from flask import Flask, render_template, request # used for jinja and getting post requests 

from todo_app.flask_config import Config # not sure what this does

from todo_app.data.session_items import * # can use * as a wildcard to take everything from another file



app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
#@app.route('/newitem', methods=['GET', 'POST'])
def index():
    items_variable = get_items()
    return render_template('index.html', items=items_variable)


@app.route('/newitem', methods=['POST'])
def addNewItem():
    newItem = request.form['createNew']
    add_item(title = newItem)
    items_variable = get_items()
    return render_template('index.html', items=items_variable)
      

if __name__ == '__main__':
    app.run()
