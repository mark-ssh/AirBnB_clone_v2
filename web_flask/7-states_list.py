#!/usr/bin/python3
"""
Very Simple Flask hello world
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Inserts all States from the database to the DOM
    """
    storeall = storage.all("State").values()
    return (render_template('7-states_list.html', states=storeall))


@app.teardown_appcontext
def teardown(exception):
    """
    Tears down the db connection
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
