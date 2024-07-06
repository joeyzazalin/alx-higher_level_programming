#!/bin/bash
# this script send a request to the URL to get the size of the response body
curl -s "$1" | wc -c
