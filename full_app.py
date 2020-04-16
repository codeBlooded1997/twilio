# Import twilio
# Client creates a Client object in our python app to let us communicte with client
from twilio.rest import Client

#
from my_secret_numbers import my_auth_token, my_cell_number

# for csv files
import pandas as pd


# Codes required by twiliio. These are specific to the twilio account being used.
account_sid = "AC81b4362f605c6398a48da412dcff6926"
auth_token = my_auth_token

# Make our twilio Client (Unoque to out account)
client = Client(account_sid, auth_token)

#
sender = "+16194326457"
# Reads the csv file with the columns that we want and we pick out the column and pass it to the list ans slice the first item
numbers = pd.read_csv('numbers.csv', names=['phone']).phone.tolist()[1:]
blacklist = pd.read_csv('blacklist.csv', names=['phone']).phone.tolist()[1:]
receivers = list(set(numbers).difference(set(blacklist)))

# Broadcast the initial text to get subscribers aware.
def broadcast():
    for receiver in receivers:
        # The text that we will text out
        text = "🔥🔥🔥\n\nHey there subscriber! Do you want to check out our new youtube video?" + \
               "\n\nReply Y to be given the link." + \
               "\n\nReply B to be blacklisted and stop receiving texts from us."

        # Use the client to send the SMS text
        client.messages.create(to=receiver, from_=sender, body=text) # create method, creates and sends sms in one step





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
    print(automatic_response)

    # Return message to our flask website
    return str(automatic_response)

# Linking a specific url to function
web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['GET', 'POST'])   # When ew get to '/' url call flask_url function

# Code starts here
if __name__ == '__main__':   # If we run this from commandline, then run the app

    # Broadcast initial text
    broadcast()
    # Run this flask app on our local server 5000
    web_app.run()
