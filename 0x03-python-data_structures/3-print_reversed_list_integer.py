#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - pprint list in reverse
    @my_list: list
    """
    msu = len(my_list)
    start = -1
    while True:
        print("{}".format(my_list[start]))
        start -= 1
        if start + msu == 0:
            break
