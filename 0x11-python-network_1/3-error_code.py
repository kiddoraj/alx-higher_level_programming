#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

# Check if a URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except Exception as e:
    print("Error:", e)
