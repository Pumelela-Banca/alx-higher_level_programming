#!/usr/bin/python3

"""
module converts all class attributes to json format
"""


def class_to_json(obj):
    """
    class to json converter class
    """

    return obj.__dict__

