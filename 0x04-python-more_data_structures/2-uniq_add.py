
def uniq_add(my_list=[]):
    """
    uniq_add - add all unique elements
    @my_list: list
    Return: sum
    """
    if len(my_list) == 0:
        return 0
    elif len(my_list) == 1:
        return my_list[0]
    else:
        don = set(my_list)
        opp = 0
        for x in don:
            opp += x
        return opp
