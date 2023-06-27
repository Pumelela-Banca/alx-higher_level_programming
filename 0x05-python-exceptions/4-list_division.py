#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides list index by each
    @my_list_1: list 1
    @my_list_2: list 2
    @list_length: amount to divisions
    Return: new list
    """
    new = [1] * list_length
    no = 0
    for x in range(0, list_length):
        try:
            no = my_list_1[x] / my_list_2[x]
        except TypeError: 
            new[x] = 0
            print("wrong type")
            continue
        except ZeroDivisionError:
            new[x] = 0
            print("division by 0")
            contnue
        except IndexError:
            new[x] = 0
            print("out of range")
            continue
        finally:
            new[x] = no
    return new
