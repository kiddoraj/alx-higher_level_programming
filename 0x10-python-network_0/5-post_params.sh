#!/bin/bash
# This script sends a POST request to a URL with custom variables in the request body and displays the response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
