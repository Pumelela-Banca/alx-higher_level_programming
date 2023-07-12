#!/usr/bin/python3

"""
module with function that saves file to json format
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes Object to json file
    """
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
