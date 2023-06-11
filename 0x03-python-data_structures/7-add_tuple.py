#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - adds index (1, 2) from two tuples
    @tuple_a: tuple
    @tuple_b: tuple
    Return: tuple with two interges
    """
    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        return (,)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
