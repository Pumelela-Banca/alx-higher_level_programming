#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints integer
    @value: print this
    @Return: True for integer and false for other
    """
    try:
        print("{:d}".format())
    except IndexError:
        return False
    else:
        return True