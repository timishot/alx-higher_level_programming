#!/usr/bin/python3
"""Python script that takes in a URL"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_id = response.getheader('X-Request-Id')
        print(x_id)
