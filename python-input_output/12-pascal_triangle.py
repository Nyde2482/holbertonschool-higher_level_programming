#!/usr/bin/python3
"""Module that contains the pascal_triangle function."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    result_list = []
    if n <= 0:
        return result_list

    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(result_list[i-1][j-1] + result_list[i-1][j])
        result_list.append(line)
    return result_list
