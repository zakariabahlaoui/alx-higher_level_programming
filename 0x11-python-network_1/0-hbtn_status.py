#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""
import urllib.request

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Fetching the URL
with urllib.request.urlopen(url) as response:
    # Reading the response body
    content = response.read()

    # Decoding the content to utf-8
    utf8_content = content.decode('utf-8')

    # Displaying the response body
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)
