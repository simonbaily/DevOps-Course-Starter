from flask import Flask, render_template

from todo_app.flask_config import Config

from .data.session_items import get_items, _DEFAULT_ITEMS

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/item')
def index():
    items = get_items()
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run()
