#!/usr/bin/python3
"""
Working module of a Pascal's triangle.
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for b in range(n):
        row = []
        for c in range(b + 1):
            if c == 0 or c == b:
                row.append(1)
            else:
                row.append(triangle[b - 1][c - 1] + triangle[b - 1][c])
        triangle.append(row)

    return triangle
