#!/bin/bash
# This script sends a GET request to a URL with a custom header and displays the response body

# Check if a URL is provided as the first argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL to send the GET request to
url="$1"

# Send a GET request with the custom header using curl and display the response body
curl -s -H "X-School-User-Id: 98" "$url"
