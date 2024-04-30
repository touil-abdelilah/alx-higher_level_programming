#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Send a request to the URL using curl and store the response body in a variable
response=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')

# Display the size of the body of the response
echo "$response"
