#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - square items in a list
    @matrix: array
    """
    if len(matrix) == 1:
        return []
    else:
        return [[y**2 for y in x] for x in matrix]
