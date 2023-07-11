#!/usr/bin/python3

"""
a module with function that appends string to end of text file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a") as file:
        file.write(text)

    with open(filename, "r") as file:
        lines = file.readlines()
    return len(lines[-1])
