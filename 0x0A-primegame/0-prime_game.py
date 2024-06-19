#!/usr/bin/python3
"""prime game module
"""


def get_primes(n, primes_memo):
    """gets the winner of a prime game
    where x is the number of rounds and nums is an array of n
    """
    primes = [True for _ in range(n + 1)]
    p = 2
    if len(primes_memo) > 0:
        if n < primes_memo[len(primes_memo) - 1]:
            return
        p = primes_memo[len(primes_memo) - 1]

    while (p * p) <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    for i in range(2, n + 1):
        if primes[i]:
            if len(primes_memo) > 0:
                if primes_memo[len(primes_memo) - 1] < i:
                    primes_memo.append(i)
            else:
                primes_memo.append(i)


def isWinner(x, nums):
    primes_memo = []
    """gets the winner of a prime game
    where x is the number of rounds and nums is an array of n
    """
    prev_len = 0
    winner = [0,  0]
    streak = True
    for i in range(x):
        n = nums[i]
        get_primes(n, primes_memo)

        if len(primes_memo) != prev_len:
            streak = not streak
            prev_len = len(primes_memo)
        winner[int(streak)] += 1

    return 'Ben' if winner[1] > winner[0] else 'Maria'
