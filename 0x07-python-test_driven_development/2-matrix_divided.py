#!/usr/bin/python3

"""
function that divides matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    divide all elements of matrix by div
    :param matrix: two-dimensional list
    :param div: num to use
    :return: new matrix divided
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list) or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    num_1 = [0.00] * len(matrix)
    size = len(matrix[0])

    for x in range(0, len(matrix)):
        if len(matrix[x]) != size:
            raise TypeError(
                "Each row of the matrix must have the same size")
        num_1[x] = [0.00] * len(matrix[x])
        for i in range(0, len(matrix[x])):
            s = matrix[x][i] / div

            num_1[x][i] = round(s, 2)

    return num_1
