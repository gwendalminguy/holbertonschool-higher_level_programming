#!/usr/bin/python3

"""
Module containing...
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Parameters:
    m_a (list of lists): first matrix
    m_b (list of lists): second matrix

    Return: new matrix as product of m_a by m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_b should contain only integers or floats")

    height_a = len(m_a)
    width_a = len(m_a[0])
    for i in m_a:
        if len(i) != width_a:
            raise TypeError("each row of m_a must be of the same size")

    height_b = len(m_b)
    width_b = len(m_b[0])
    for i in m_b:
        if len(i) != width_b:
            raise TypeError("each row of m_b must be of the same size")

    if width_a != height_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new = []

    for i in range(height_a):
        row = []
        for j in range(width_b):
            result = 0
            for k in range(width_a):
                result += m_a[i][k] * m_b[k][j]
            row.append(result)
        new.append(row)

    return new
