#!/usr/bin/python3
# Write a Python script that takes in a letter and sends a POST request to...
import requests
import sys

# Check if a letter argument is provided, set q="" if not
if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"
data = {'q': q}

try:
    response = requests.post(url, data=data)

    # Check if the response contains valid JSON
    try:
        user_data = response.json()

        # Check if the JSON is not empty
        if user_data:
            user_id = user_data.get('id')
            user_name = user_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print("Error:", e)
