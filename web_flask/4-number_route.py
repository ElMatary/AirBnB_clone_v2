#!/usr/bin/python3
""" 4-number_route module"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """a fun to display Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """a fun to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """a fun to display c text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """a fun to display python text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """a fun to display number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
