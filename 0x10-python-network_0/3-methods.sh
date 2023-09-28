#!/bin/bash
# This script sends an HTTP OPTIONS request to a URL and displays the accepted HTTP methods
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
