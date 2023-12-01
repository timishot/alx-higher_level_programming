#!/usr/bin/python3
import urllib.request
import sys
import urllib.parse
"""sends a POST request to the passed URL """
if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    url_value = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data=url_value, method='POST')
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
