import requests
from requests.auth import HTTPBasicAuth

# This endpoint retrieves comments on a specific Instagram post based on the post ID.
# You need to provide the Instagram post's unique ID.

# API endpoint for fetching comments on a post
url = "https://boxapi.ir/api/instagram/media/get_comments"

# BoxAPI authentication credentials
username = "boxapi_username"  # Replace with your BoxAPI username
password = "boxapi_password"  # Replace with your BoxAPI password

# Data to send in the request (Instagram post ID)
data = {
    "id": 2967835229909923253  # Replace with the specific Instagram post ID
}

# Send a POST request to BoxAPI
response = requests.post(url, auth=HTTPBasicAuth(username, password), json=data)

# Check if the request was successful
if response.status_code == 200:
    # If successful, print the comments data
    print("Post Comments:", response.json())
else:
    # If there was an error, print the error status and message
    print("Failed to retrieve comments. Status code:", response.status_code)
    print("Error message:", response.text)
