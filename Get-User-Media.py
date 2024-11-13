import requests
from requests.auth import HTTPBasicAuth

# This endpoint retrieves a specified number of recent posts from an Instagram user.
# You need to provide the Instagram user's ID and the number of posts you want to fetch.

# API endpoint for fetching user media posts
url = "https://boxapi.ir/api/instagram/user/get_media"

# BoxAPI authentication credentials
username = "boxapi_username"  # Replace with your BoxAPI username
password = "boxapi_password"  # Replace with your BoxAPI password

# Data to send in the request (Instagram user ID and post count)
data = {
    "id": 12281817,    # Replace with the Instagram user ID
    "count": 12        # Number of posts to retrieve
}

# Send a POST request to BoxAPI
response = requests.post(url, auth=HTTPBasicAuth(username, password), json=data)

# Check if the request was successful
if response.status_code == 200:
    # If successful, print the media posts data
    print("User Media Posts:", response.json())
else:
    # If there was an error, print the error status and message
    print("Failed to retrieve user media. Status code:", response.status_code)
    print("Error message:", response.text)
