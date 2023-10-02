#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me using curl
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
