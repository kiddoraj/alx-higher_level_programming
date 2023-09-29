#!/usr/bin/python3
# Write a Python script that takes in a URL and an email address, sends a POST request to the...
import requests
import sys

# Check if URL and email arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email as a parameter
data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Display the body of the response
    print("Response body:")
    print(response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
