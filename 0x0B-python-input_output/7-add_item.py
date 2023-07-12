#!/usr/bin/python3

"""
script to load and add json objects to a file
"""
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file.py').save_o_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file


"""
script to create python objects to be saved in file add_item.json 
"""


if len(argv) == 1:
    with open("add_item.json", "w+") as f:
        data = json.load(f)
        if not data:
            json.dump([], f)
else:
    with open("add_item.json", "w+") as f:
        data = json.load(f)
        for x in argv[1:]:
            data.append(x)
        json.dump(data, f)
