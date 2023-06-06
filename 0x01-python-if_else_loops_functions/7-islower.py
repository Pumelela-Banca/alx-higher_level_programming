#!/usr/bin/python3

def islower(c):
    """
    islower - cheacks if c is lower case
    c: letter
    Return: True or False
    """

    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False
