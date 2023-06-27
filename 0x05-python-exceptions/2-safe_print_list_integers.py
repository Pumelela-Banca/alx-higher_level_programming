#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints first x elements of list only integers
    @my_list: list
    @x: elements to print
    return: number of elements printed
    """
    num = 0
    size = 0
    for n in my_list[:x]:
        size += 1
        try:
            print("{:d}".format(n), end="")
        except (TypeError, ValueError):
            continue
        else:
            num += 1
    if x > size:
        raise IndexError
    print()
    return num
