# Import twilio
# Client creates a Client object in our python app to let us communicte with client
from twilio.rest import Client

#
from my_secret_numbers import my_auth_token, my_cell_number

# Codes required by twiliio. These are specific to the twilio account being used.
account_sid = "AC81b4362f605c6398a48da412dcff6926"
auth_token = my_auth_token

# Make our twilio Client (Unoque to out account)
client = Client(account_sid, auth_token)

#
sender = "+16194326457"
receiver = my_cell_number

# The text that we will text out
text = "Yo, wassup."

# Use the client to send the SMS text
client.messages.create(to=receiver, from_=sender, body=text) # create method, creates and sends sms in one step
