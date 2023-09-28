#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL to send the request to
url="$1"

# Send a request using curl and extract the status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Display the status code
echo "Status Code: $response"
