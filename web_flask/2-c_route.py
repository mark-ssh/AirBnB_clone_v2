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


@app.route('/c/<value>', strict_slashes=False)
def c_is(value):

    """
    Returns the route /c/<value>
    where <value> is any URL that the user requests
    """
    return ("C {:s}".format(value.replace("_", " ")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
