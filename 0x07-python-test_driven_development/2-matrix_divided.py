#!/usr/bin/python3

""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    divide matrix number by div
    Args:
        matrix : the first number
        div : the second number
    Returns:
        new_matrix
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    TypeErr = "matrix must be a matrix (list of lists) of integers/floats"
    if not type(matrix) is list:
        raise TypeError(TypeErr)
    len_matrix = len(matrix[0])
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if not type(j) in [int, float]:
                raise TypeError(TypeErr)
        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
    res = [[a / div for a in row] for row in matrix]
    new_matrix = [[round(a, 2) for a in row] for row in res]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
