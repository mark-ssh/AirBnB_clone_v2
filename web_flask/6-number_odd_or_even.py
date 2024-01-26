#!/usr/bin/python3
"""
Very simple Flask hello world
"""

from flask import Flask
from flask import render_template

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

@app.route('/number/<int:n>', strict_slashes=False)
def number_is(n):

    """
    Displays /number/<n> URI only if it is an integer
    """
    return("{:d} is a number".format(n))

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):

    """
    Displays the template 5-number.html
    if /number_template/<n> URI is requested
    and if it is an integer
    """
    return(render_template('5-number.html', n=n))

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_template(n):

    """
    Displays the template 6-number_odd_or_even.html
    if /number_odd_or_even/<n> URI is requested
    and if it is an integer
    """
    string = "odd" if n % 2 else "even"
    return(render_template('6-number_odd_or_even.html', n=n, string=string))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
