#!/usr/bin/python3
"""sends a POST request to the passed URL """
import urllib.request
import sys
import urllib.parse
<<<<<<< HEAD
"""sends a POST request to the passed URL """
"""if __name__ == "__main__":
=======
if __name__ == "__main__":
>>>>>>> a8af6a1f4e8ccfeccae5ae0e931638e02729191e
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    url_value = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data=url_value, method='POST')
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)"""

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Create a POST request with the specified data
        request = urllib.request.Request(url, data=data, method='POST')

        with urllib.request.urlopen(request) as response:
            # Decode and print the body of the response
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
        sys.exit(1)

