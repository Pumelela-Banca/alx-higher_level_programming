#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - square items in a list
    @matrix: array
    """
    if len(matrix) == 0:
        return []
    if len(matrix) == 1 and matrix[0] is []:
        return [[]]
    else:
        return [[y**2 for y in x] for x in matrix]
