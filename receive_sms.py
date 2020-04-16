# Import the flask framework
from flask import Flask

# Class in twillion that allows us to response to the text messages when someone text to our twilio phone number
# This is needed to responde to any texts the come in
from twilio.twiml.messaging_response import MessagingResponse

# Create our flask app
web_app = Flask(__name__)

#
def sms_reply():

    # Create a response object (translates string to twiml for us. Twilio excpects twiml.)
    automatic_response = MessagingResponse()

    # Put a message in our response object
    automatic_response.message("This is an autoreply from Python 🐍 and Twilio 🟪.")
    pritn(automatic_response)

    # Return message to our flask website
    return str(automatic_response)

# Linking a specific url to function
web_app.add_url_rule('/sms', 'sms_reply', sms_reply)   # When ew get to '/' url call flask_url function

# Code starts here
if __name__ == '__main__':   # If we run this from commandline, then run the app
    # Run this flask app on our local server 5000
    web_app.run()
