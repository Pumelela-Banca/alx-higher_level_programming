#!/usr/bin/python3

"""
a module with function that writes a file
"""


def write_file(filename="", text=""):
    """
    write to a file the text
    :param filename:File to write on
    :param text: characters to write
    :return: number of characters written
    """
    lines = []
    size = 0
    with open(filename, "w") as file:
        file.write(text)
    with open(filename, "r") as file:
        lines = file.readlines()
        for x in range(0, len(lines)):
            size += lenx(x)
    return size
