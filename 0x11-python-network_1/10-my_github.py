#!/usr/bin/python3
# Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
import requests
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

# Create a Basic Authentication header with your username and PAT
headers = {
    'Authorization': f'Basic {username}:{access_token}',
}

# Make a GET request to the GitHub API to fetch your user information
url = 'https://api.github.com/user'
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response and display your user ID
    user_data = response.json()
    user_id = user_data.get('id')
    print(f"Your GitHub user ID is: {user_id}")

except requests.exceptions.RequestException as e:
    print("Error:", e)
