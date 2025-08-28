import requests

def post_to_facebook(access_token, message):
    """
    Post text to Facebook
    
    Args:
        access_token (str): Facebook API access token
        message (str): Text content to post
    
    Returns:
        bool: True if successful, False otherwise
    """
    
    url = "your facebook url"
    
    data = {
        "message": message,
        "access_token": access_token
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Post created successfully!")
        return True
    else:
        print(f"Failed to create post: {response.text}")
        return False

# Usage
if __name__ == "__main__":
    # Replace with your Facebook access token
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
    
    # Your post message
    POST_MESSAGE = "Hello Facebook, im Harshwardhan! This post was created using Python! 🚀"
    
    # Post to Facebook
    post_to_facebook(ACCESS_TOKEN, POST_MESSAGE)
