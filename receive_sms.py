# Import the flask framework
from flask import Flask

# Create our flask app
web_app = Flask(__name__)

#
def flask_url():
    return "Hello"

# Linking a specific url to function
web_app.add_url_rule('/Y', 'flask_url', flask_url)   # When ew get to '/' url call flask_url function

web_app.run()
