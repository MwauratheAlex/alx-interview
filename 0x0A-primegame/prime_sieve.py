#!/usr/bin/python3
import timeit
"""
-------Sieve of Eratosthenes
Given a number n, print all primes smaller than or equal to n.
It is also given that n is a small number.

Example:
Input : n =10
Output : 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19

The sieve of Eratosthenes is one of the most efficient ways to find all primes
smaller than n when n is smaller than 10 million or so.
"""


def seiveOfEratosthenes(n):
    # create a boolean array prime[0...n]
    prime = [True for _ in range(n + 1)]
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p]:
            print(p)


n = 10000000
seiveOfEratosthenes(n)

elapsed_time = timeit.timeit(lambda: seiveOfEratosthenes(n), number=1)

print(f"It took {elapsed_time}")
