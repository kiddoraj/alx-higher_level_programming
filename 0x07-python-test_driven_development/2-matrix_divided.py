#!/usr/bin/python3
"""
This module contains a function that divides the numbers of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides the integer/float numbers of a matrix.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If the elements of the matrix are not lists, or if the elements of the lists are not integers/floats.
        TypeError: If div is not an integer/float number.
        TypeError: If the lists of the matrix do not have the same size.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not isinstance(num, (int, float)):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m

