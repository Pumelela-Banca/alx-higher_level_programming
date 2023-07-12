#!/usr/bin/python3

"""
module with function converts json string from python
"""


def from_json_string(my_str):
    """
    creates python object from JSON string
    """
    new = ''
    for x in my_str:
        if x == '\n':
            continue
        new += x
    return eval(my_str)
