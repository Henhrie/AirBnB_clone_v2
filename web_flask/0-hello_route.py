#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Function """
    # Start the Flask development server
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)
