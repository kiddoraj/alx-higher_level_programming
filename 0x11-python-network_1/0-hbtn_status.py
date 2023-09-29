#!/usr/bin/python3
# Script to featch data from a webpage
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data.decode('utf-8'))
except Exceptions as e:
      print(e)
