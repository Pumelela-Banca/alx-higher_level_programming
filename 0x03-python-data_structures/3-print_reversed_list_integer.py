
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - pprint list in reverse
    @my_list: list
    """
    msu = len(my_list)
    if msu == 0:
        print([])
    start = -1
    while True:
        print("{:d}".format(my_list[start]))
        start -= 1
        if start + msu == -1:
            break
