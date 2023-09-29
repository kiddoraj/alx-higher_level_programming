#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
