#!/usr/bin/python3
import urllib.request
import sys
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_id = response.getheader('X-Request-Id', 'Not Present')
        print(x_id)
