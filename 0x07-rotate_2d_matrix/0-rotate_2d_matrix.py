#!/usr/bin/python3
"""Rotate 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate two dimension matrix 90 degrees clockwise

    Args:
        matrix (list of list of int): The two dimension matrix to rotate.
        Assumes a square matrix.
    """
    n = len(matrix)

    # Swap elements of each row and column
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
