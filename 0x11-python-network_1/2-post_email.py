#!/usr/bin/python3

"""
enters field in a web
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    new_str = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(
        sys.argv[1], data=new_str, method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
