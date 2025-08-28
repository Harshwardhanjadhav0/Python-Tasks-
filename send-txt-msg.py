from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'ACcddacf7b0605d57eaadd37675482c7d3'
auth_token = '3975ad2b79088bebb9f5ce760299c698'

# Create a client to interact with the Twilio API
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body="Hello from Harsh using python !",
    from_='+your no.',  # Your Twilio number
    to='+918668396959'        # Recipient's phone number
)

print(f"Message sent with SID : {message.sid}")
