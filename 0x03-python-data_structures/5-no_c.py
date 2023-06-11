#!/usr/bin/python3

def no_c(my_string):
    """
    no_c - replaces all Cc
    @my_string: string
    """
    hold = ''
    for x in my_string:
        if x in 'Cc':
            continue
        hold += x
    return hold
