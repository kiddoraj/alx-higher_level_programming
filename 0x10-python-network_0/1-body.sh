#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response if it has a 200 status code

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request using curl and store the response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the response has a 200 status code (OK)
if [ "$response" -eq 200 ]; then
  curl -s "$1"
else
  echo "Error: Received HTTP status code $response"
fi
