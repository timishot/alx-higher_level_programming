#!/usr/bin/python3
"""X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_requests_id = response.headers['X-Request-Id']
    print(x_requests_id)
