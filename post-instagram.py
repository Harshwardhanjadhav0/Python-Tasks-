from instagrapi import Client
import getpass

def post_on_instagram():
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    photo_path = input("Enter the path to the photo you want to upload: ")
    caption = input("Enter the caption for the photo: ")

    # Initialize the client
    client = Client()

    # Login to Instagram
    client.login(username, password)

    # Upload the photo with the caption
    media = client.photo_upload(photo_path, caption=caption)

    # Extract media ID
    

    print(f"Photo uploaded successfully! Media ID: {media.id}")

if __name__ == "__main__":
    post_on_instagram()
