#!/bin/bash
# this script takes URL, send a POST request to display body response
curl -sL -X POST -d "email=test@gmail.com&subject=i will always be here for PLD" "$1"
