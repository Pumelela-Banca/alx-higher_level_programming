#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    search_replace - replace element in a list
    @my_list: is the initial list
    @search: is the element to replace in the list
    @replace: is the new element
    """
    if len(my_list) == 0:
        return my_list
    elif search not in my_list:
        return my_list
    else:
        return [replace if x == search else x for x in my_list]
