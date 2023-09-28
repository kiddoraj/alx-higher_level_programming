#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the size of the response body in bytes using curl
response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}')
if [ -z "$response_size" ]; then
  echo "Unable to retrieve response size."
else
  echo "Response Size: $response_size bytes"
fi
