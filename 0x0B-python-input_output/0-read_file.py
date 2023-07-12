#!/usr/bin/python3

"""
a module with function that reads from a file
"""


def read_file(filename=""):
    """
    function prints lines of a list
    :param filename: file to read
    """
    with open(filename, 'r') as file:
        for x in file:
            print(x, end="")
