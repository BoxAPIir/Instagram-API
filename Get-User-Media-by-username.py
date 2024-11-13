import requests
from requests.auth import HTTPBasicAuth

# This endpoint retrieves a specified number of recent posts from an Instagram user based on their username.
# You need to provide the Instagram username and the number of posts you want to fetch.

# API endpoint for fetching user media posts by username
url = "https://boxapi.ir/api/instagram/user/get_media_by_username"

# BoxAPI authentication credentials
username = "boxapi_username"  # Replace with your BoxAPI username
password = "boxapi_password"  # Replace with your BoxAPI password

# Data to send in the request (Instagram username and post count)
data = {
    "username": "Boxapi.ir",  # Replace with the Instagram username
    "count": 12               # Number of posts to retrieve
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
