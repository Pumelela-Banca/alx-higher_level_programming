#!/usr/bin/python3

"""
module with function converts json string from python
"""


def from_json_string(my_str):
    """
    creates python object from JSON string
    """
    return eval(my_str)
