import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
def send_mssg(number, message):
    account_sid = 'AC6b46521ddc9d177f3f6e23d3b5e87191'
    auth_token = '4d6b6cbe9cdbefd455c45773b68c9e02'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=message,
             from_='+19284874293',
             to= '+1'+str(number)
         )

    print(message.sid)
