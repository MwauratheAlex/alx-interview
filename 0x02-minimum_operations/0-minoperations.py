#!/usr/bin/python3
"""This module contains the function minOperations"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in a file.
    In the text file, there is a single character H.
    Your text editor can execute only two operations in this file:
        Copy All and Paste.
    args:
        n: (int) no of characters
    Return: the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    if n <= 0:
        return 0
    operations = 0
    divisor = 2  # lowest prime

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1
    return operations
