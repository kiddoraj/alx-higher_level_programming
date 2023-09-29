#!/usr/bin/python3
# Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
import requests
import sys

# Check if a URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    # Check the HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Display the body of the response
        print("Response body:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
