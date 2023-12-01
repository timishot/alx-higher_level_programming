#!/usr/bin/python3
import urllib.request
"""print(f"    - type: {type(content)}")"""
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    content = response.read()
print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    - utf8 content: {content.decode('utf-8')}")
