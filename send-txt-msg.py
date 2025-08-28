from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = ' your account_sid of twilio'
auth_token = ' twilio auth token '

# Create a client to interact with the Twilio API
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body="Hello from Harsh using python !",
    from_='+your no.',  # Your Twilio number
    to='+918668396959'        # Recipient's phone number
)

print(f"Message sent with SID : {message.sid}")
