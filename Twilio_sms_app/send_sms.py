from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio


# Find these values at https://twilio.com/user/account
def send_message():
    to_number = input('To whom do you want to send: ')
    message = input('What do you want send: ')
    client = Client(account_sid, auth_token)

    my_msg = "Hello body how are you"

    message = client.messages.create(to=to_number, from_=my_twilio, body=message)


send_message()
