#!/usr/bin/python3
"""sends a POST request to the passed URL """
import urllib.request
import sys
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    try:
        request = urllib.request.Request(url, data=data, method='POST')

        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
        sys.exit(1)

