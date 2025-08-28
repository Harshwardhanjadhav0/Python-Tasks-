import requests
import json

def post_to_linkedin(access_token, text):
    """
    Post text to LinkedIn
    
    Args:
        access_token (str): LinkedIn API access token
        text (str): Text content to post
    
    Returns:
        bool: True if successful, False otherwise
    """
    
    # Get user ID
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    profile_response = requests.get("https://api.linkedin.com/v2/people/~", headers=headers)
    
    if profile_response.status_code != 200:
        print("Failed to get user profile")
        return False
    
    user_id = profile_response.json()['id']
    
    # Create post
    post_data = {
        "author": f"urn:li:person:{user_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    post_response = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers=headers,
        data=json.dumps(post_data)
    )
    
    if post_response.status_code == 201:
        print("Post created successfully!")
        return True
    else:
        print(f"Failed to create post: {post_response.text}")
        return False

# Usage
if __name__ == "__main__":
    # Replace with your LinkedIn access token
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
    
    # Your post text
    POST_TEXT = "Hello LinkedIn, I'm Harshwardhan! This post was created using Python! 🚀"
    
    # Post to LinkedIn
    post_to_linkedin(ACCESS_TOKEN, POST_TEXT)
