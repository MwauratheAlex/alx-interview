#!/usr/bin/env python3
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
    current_h_count = 1
    copied_h_count = 0
    steps = 0

    while current_h_count < n:
        if n % current_h_count == 0:
            # copy
            copied_h_count = current_h_count
            steps += 1
            # paste
            current_h_count += copied_h_count
            steps += 1
        else:
            # paste
            current_h_count += copied_h_count
            steps += 1

    return steps
