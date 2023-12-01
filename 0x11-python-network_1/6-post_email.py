#!/usr/bin/python3
"""Python script that takes in a URL"""
import requests
import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		exit(1)
	url = sys.argv[1]
	email = sys.argv[2]
	emails = {'email': email}
	r = requests.post(url, email=emails)
	print(r.text)
