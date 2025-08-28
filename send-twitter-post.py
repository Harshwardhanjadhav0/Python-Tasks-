import tweepy
bearer_token = "YOUR_BEARER_TOKEN"
consumer_key = "YOUR_API_KEY"
consumer_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
client = tweepy.Client(
 bearer_token=bearer_token,
 consumer_key=consumer_key,
 consumer_secret=consumer_secret,
 access_token=access_token,
 access_token_secret=access_token_secret
)
response = client.create_tweet(text="Hello Twitter from Python by Harshwardhan!")
print("Tweet posted! Tweet ID:", response.data['id'])
