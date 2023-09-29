#!/usr/bin/python3
# Write a Python script that takes in a URL, sends a request to the ...
import requests
import sys

# Check if a URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Check if the 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id header not found in the response.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
