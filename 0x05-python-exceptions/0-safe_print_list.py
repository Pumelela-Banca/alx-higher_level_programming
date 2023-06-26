#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    prints x elements in a list
    @my_list: list
    @x: elements to print
    Return: number of elements printed
    """
    num = 0
    try:
        for n in my_list:
            print(n, end="")
            num += 1
    except IndexError:
        pass
    print()
    return num
