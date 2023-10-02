#!/usr/bin/python3
# Write a Python script that takes in a URL and an email address, sends a POST request to the...
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
