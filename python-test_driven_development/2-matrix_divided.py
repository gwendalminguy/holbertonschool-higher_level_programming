#!/usr/bin/python3

"""
2-matrix_divided.py
Module containing a function dividing a matrix by an integer.
Returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides each integer from a matrix by another integer.

    Parameters:
    matrix (list): list of lists of integers to divide
    div (int): integer to use as divisor

    Return: new matrix of the results
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix "
            "(list of lists) of integers/floats")
    for i in range(len(matrix)):
        if i == 0:
            length = len(matrix[i])
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(
                    matrix[i][j], float):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")
        if length != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda x: round(x / div, 2), matrix[i]))
    return new
