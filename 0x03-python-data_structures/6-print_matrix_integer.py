

def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - prints matrix
    @matrix: data
    """
    if matrix == [[]]:
        print()
        return
    if isinstance(matrix[0], list):
        for x in matrix:
            print_matrix_integer(x)
    else:
        str = ""
        for x in matrix[0:-1]:
            str += "{:d} ".format(x)
        str += "{:d}".format(matrix[-1])
        print(str)
