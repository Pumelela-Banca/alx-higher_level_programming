#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - prints matrix
    @matrix: data
    """
    str = '' # save to remove last space
    for row in matrix:
        for col in row:
            str += "{} ".format(col)
        str = str[:-1]
        print(str)
