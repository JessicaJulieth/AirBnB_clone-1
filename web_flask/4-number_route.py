#!/usr/bin/python3
"""
    starts a Flask web application
"""

from flask import Flask
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


@app.route("/number/<n>", strict_slashes=False)
def is_num(n):
    """
    Returns:The default value of text is “is cool”
    """
    if isistant(n, int)
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
