#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response, sends variables
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
