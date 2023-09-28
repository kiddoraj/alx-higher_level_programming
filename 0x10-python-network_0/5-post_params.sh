#!/bin/bash
# This script sends a POST request to a URL with custom variables in the request body and displays the response body

# Check if a URL is provided as the first argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL to send the POST request to
url="$1"

# Define the variables to be sent in the request body
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with the custom variables in the request body using curl and display the response body
curl -s -X POST -d "email=$email&subject=$subject" "$url"
