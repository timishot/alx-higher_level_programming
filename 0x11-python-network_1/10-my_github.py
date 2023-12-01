#!/usr/bin/python3
"""Python script that takes your GitHub credentials """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit(1)

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code == 200:
        user_data = r.json()
        print(user_data['id'])
    else:
        print(None)
