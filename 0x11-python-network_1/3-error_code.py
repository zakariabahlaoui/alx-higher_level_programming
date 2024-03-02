#!/usr/bin/python3
""" 
Script that takes in a URL, send a request to URL, and dispaly body
"""

import urllib.request
import urllib.error
import sys

# Function to handle HTTP errors and print the error code
def handle_error(e):
    print("Error code:", e.code)

# URL to fetch
url = sys.argv[1]

# Sending a request to the URL
try:
    with urllib.request.urlopen(url) as response:
        # Reading the response body and decoding it in utf-8
        body = response.read().decode('utf-8')
        print(body)

# Handling HTTP errors
except urllib.error.HTTPError as e:
    handle_error(e)
