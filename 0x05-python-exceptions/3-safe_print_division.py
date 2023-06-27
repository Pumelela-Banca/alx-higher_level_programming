#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divide two numbers
    @a: int
    @b: int
    Return: result of division
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
