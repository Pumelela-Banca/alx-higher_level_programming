#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    delete_at - deletes index
    @my_list: list
    @idx: index to delete
    Return: new list
    """
    if idx < 0 or idx >= len(my_list) or len(my_list) == 0:
        return my_list
    del my_list[idx]
    return my_list
