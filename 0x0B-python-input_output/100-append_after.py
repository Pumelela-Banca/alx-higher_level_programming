#!/usr/bin/python3

"""
module contains function to insert text into a file
after a line containing a new string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    unction that inserts a line of text to a file, after each
    line containing a specific string
    """
    new = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for ln in lines:
            new.append(ln)
            if search_string in ln:
                new.append([new_string])

    with open(filename, 'w') as f:
        for x in new:
            f.writelines(x[0])
