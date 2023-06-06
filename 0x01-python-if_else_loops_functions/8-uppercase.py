#!/usr/bin/python3

def uppercase(str):
    """
    uppercase - converts string to uppercase
    str: string
    Return: void
    """
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            print("{:c}".format(ord(x) - 32), end='')
        else:
            print(x, end='')
    print()
