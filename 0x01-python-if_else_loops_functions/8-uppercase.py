#!/usr/bin/python3

def uppercase(str):
    """
    uppercase - converts string to uppercase
    str: string
    Return: void
    """
    oh = 0
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            oh = ord(x) - 32
        else:
            oh = ord(x)
        print("{:c}".format(oh), end='')
    print()
