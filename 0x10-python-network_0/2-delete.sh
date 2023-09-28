#!/bin/bash
# This script sends a DELETE request to a URL and displays the body of the response
# Send a DELETE request using curl and display the response body
curl -sX DELETE -s "$1"
