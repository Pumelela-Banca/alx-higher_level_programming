#!/usr/bin/python3

"""
module with function converts json object to python
"""

import json


def load_from_json_file(filename):
    """
    unction that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
