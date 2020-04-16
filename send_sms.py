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

for receiver in receivers:
    # The text that we will text out
    text = "🔥🔥🔥\n\nHey there subscriber! Do you want to check out our new youtube video?" + \
           "\n\nReply Y to be given the link." + \
           "\n\nReply B to be blacklisted and stop receiving texts from us."

    # Use the client to send the SMS text
    client.messages.create(to=receiver, from_=sender, body=text) # create method, creates and sends sms in one step
