#!/bin/bash
# This script sends an HTTP OPTIONS request to a URL and displays the accepted HTTP methods

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an HTTP OPTIONS request using curl and display the accepted methods
curl -s -I -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
