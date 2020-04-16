# Import the flask framework
from flask import Flask

# Create our flask app
web_app = Flask(__name__)

#
def sms_reply():
    return "This is an autoreply from Python 🐍 and Twilio 🟪."

# Linking a specific url to function
web_app.add_url_rule('/sms', 'sms_reply', sms_reply)   # When ew get to '/' url call flask_url function

web_app.run()
