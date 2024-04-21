#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C' followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Displays 'Python' followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer
    """
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, odd_or_even="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, odd_or_even="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
