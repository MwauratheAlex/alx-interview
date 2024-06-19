#!/usr/bin/python3
"""prime game module
"""

primes_n = {}


def get_primes(n):
    """gets the winner of a prime game
    where x is the number of rounds and nums is an array of n
    """
    if n in primes_n:
        return primes_n[n]

    primes = [True for _ in range(n + 1)]
    p = 2

    while (p * p) <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    primes_n[n] = []
    for i in range(2, n + 1):
        if primes[i]:
            primes_n[n].append(i)

    return primes_n[n]


def isWinner(x, nums):
    """gets the winner of a prime game
    where x is the number of rounds and nums is an array of n
    """
    ben = 0
    maria = 0
    for i in range(x):
        n = nums[i]
        p_n = get_primes(n)
        if len(p_n) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben == maria:
        return None

    return 'Ben' if ben > maria else 'Maria'
