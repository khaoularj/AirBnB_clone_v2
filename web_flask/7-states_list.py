#!/usr/bin/python3
"""this script starts a Flask web app"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """function that display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present
    in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>"""
    state = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    """function that handle @app.teardown_appcontext
    closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
