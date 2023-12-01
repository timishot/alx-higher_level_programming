#!/usr/bin/python3
"""Python script that takes in a URL"""
import requests
import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		exit(1)
	url = sys.argv[1]
	email = sys.argv[2]
<<<<<<< HEAD
	emails = {'email': email}
	r = requests.post(url, email=emails)
	print(r.text)
=======
	payload = {'email': email}
	r = requests.post(url, data=payload)
	print(r.text)
>>>>>>> 15d0a39ad9f4393c35d6e7d36091a633691c2f35
