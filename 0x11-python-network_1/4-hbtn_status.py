#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
	r = requests.get('https://alx-intranet.hbtn.io/status')
	print(f"Body response:")
	print(f"\t- type: {type(r.text)}")
	print(f"\t- content: {r.text}")