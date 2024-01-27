#!/usr/bin/python3
"""this script starts a Flask web app"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """function that display HELLO HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """function that display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """function that display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text):
    """function that display “Python ”,
    followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Number(n):
    """function that display “n is a number” only if n is an integer"""
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def N_template(n):
    """function that display a HTML page only if n is an integer
    with H1 tag: “Number: n” inside the tag BODY"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
