#!/usr/bin/python3
"""This module contains the function isWinner."""

is_prime_memo = {}


def isPrime(n):
    """checks if number is prime
    Primes are only divisible by 1 and itself"""
    if n in is_prime_memo:
        return is_prime_memo[n]
    if n <= 1:
        is_prime_memo[n] = False
        return False
    for i in range(2, n):
        if n % i == 0:
            is_prime_memo[n] = False
            return False
    is_prime_memo[n] = True
    return is_prime_memo[n]


primes_memo = {}


def getPrimes(n):
    if n in primes_memo:
        return primes_memo[n]
    primes = []
    for i in range(1, n + 1):
        if isPrime(i):
            primes.append(i)
    primes_memo[n] = primes
    return primes


def isWinner(x, nums):
    """Returns the winner of a prime game"""
    if type(x) is not int:
        return None
    wins = {'Ben': 0, 'Maria': 0}
    for i in range(x):
        stop = nums[i]
        primes = getPrimes(stop)
        if len(primes) % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Ben'] == wins['Maria']:
        return None

    return 'Ben' if wins['Ben'] > wins['Maria'] else 'Maria'
