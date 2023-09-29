#!/usr/bin/python3

"""
uses requests to contact web
"""
import requests

r = requests.get(
    "https://alx-intranet.hbtn.io/status")
con = r.content
print("Body response:")
print(f"\t- type: {type(con)}")
print(f"\t- content: {con}")
