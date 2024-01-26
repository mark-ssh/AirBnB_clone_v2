#!/usr/bin/python3
"""
Very Simple Flask hello world
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():

    """
    Just returns text
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    """
    Returns the route /hbnb
    """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):

    """
    Returns the route /c/<text>
    where <text> is any URL that the user requests
    """
    return ("C {:s}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python_is(text="is cool"):

    """
    Returns the route /python/<text>
    where <value> is any URI that the user requests
    """
    return ("Python {:s}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
