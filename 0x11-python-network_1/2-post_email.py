#!/usr/bin/python3

"""
enters field in a web
"""
import sys
from urllib import request


if __name__ == "__main__":
    with request.post(
            sys.argv[1], sys.orig_argv[2]) as response:
        new = response.text.decode('utf-8')
        print(
            f'Your email is: {new}')
