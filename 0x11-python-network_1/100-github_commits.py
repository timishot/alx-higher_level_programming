#!/usr/bin/python3
""" python script that takes 2 arguments """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("complete")
        exit(1)
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    if r.status_code == 200:
        user_data = r.json()
        for i, user in enumerate(user_data[:10]):
            print(f"{user['sha']}: {user['commit']['author']['name']}")
