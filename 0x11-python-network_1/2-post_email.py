#!/usr/bin/python3
# A script to take in a url and email , sends a POST request...
import urllib.request
import urllib.parse
import sys

# Check if URL and email arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email as a parameter
data = {'email': email}
data = urllib.parse.urlencode(data).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)

except Exception as e:
    print("Error:", e)
