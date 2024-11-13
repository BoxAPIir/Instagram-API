import requests
from requests.auth import HTTPBasicAuth

# URL for the BoxAPI endpoint to get user profile information
url = "https://boxapi.ir/api/instagram/user/get_web_profile_info"

# BoxAPI authentication credentials
username = "boxapi_username"  # Replace with your BoxAPI username
password = "boxapi_password"  # Replace with your BoxAPI password

# Data to send in the request (Instagram username we want information for)
data = {
    "username": "Boxapi.ir"  # Replace with the desired Instagram username
}

# Send a POST request to BoxAPI
response = requests.post(url, auth=HTTPBasicAuth(username, password), json=data)

# Check if the request was successful
if response.status_code == 200:
    # If successful, print the returned user information
    print("User Information:", response.json())
else:
    # If there was an error, print the error status and message
    print("Failed to retrieve user info. Status code:", response.status_code)
    print("Error message:", response.text)
