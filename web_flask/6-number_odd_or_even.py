#!/usr/bin/python3
"""
    starts a Flask web application
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """
    Returns: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns:HBNB
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Returns:C
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text="is cool"):
    """
    Returns:The default value of text is “is cool”
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """
    Returns:display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Returns:display a HTML page only if n is an intege
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """
    Returns:display a HTML page only if n is an intege
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
