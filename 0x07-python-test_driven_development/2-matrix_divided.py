#!/usr/bin/python3
""" matrix_divided function module """


def matrix_divided(matrix, div):
    """ Divides all elements of matrix by div
    Args:
        matrix: list of lists containing int or float
        div: number to divide matrix by
    Return:
        list: List of lists which is diveded matrix
    Raises:
        TypeError: if matrix is not list of lists containing int or float
        TypeError: if sublists are not all same size.
        Type Error: If div is not int or gloat.
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x/div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
