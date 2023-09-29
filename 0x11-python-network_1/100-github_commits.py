#!/usr/bin/python3
# Write a Python script that takes 2 arguments in order to solve this challenge.
import requests
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

# Define the GitHub API endpoint for listing commits
api_url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

try:
    # Send a GET request to the GitHub API
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response and print the 10 most recent commits
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

except requests.exceptions.RequestException as e:
    print("Error:", e)
