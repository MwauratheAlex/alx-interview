#!/usr/bin/python3
"""This module contains the function pascal_triange(n)"""


def pascal_triangle(n):
    """
    Generates rows of Pascal's triangle up to the nth row.
    Args:
        n: integer
    Return: a list of lists of integers representing the Pascal’s triangle of n
        or returns an empty list if n <= 0
    """
    triangle = []
    if n <= 0:
        return []

    for i in range(n):
        if i <= 1:
            triangle.append([1] * (i + 1))
            continue
        new_list = []
        prev_list = triangle[i - 1]
        # sliding window sum
        window_sum = 0
        for j in range(i + 1):
            if j == 0 or j == i:
                window_sum += 1
                new_list.append(1)
            else:
                # add current value to window sum
                window_sum += prev_list[j]
                new_list.append(window_sum)
                # slide
                window_sum -= prev_list[j - 1]
        triangle.append(new_list)

    return triangle
