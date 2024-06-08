#!/usr/bin/python3

"""
makeChange - determine the fewest number of coins needed to meet a given
    amount total
Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for value in range(coin, total + 1):
            if dp[value - coin] != float('inf'):
                dp[value] = min(dp[value], 1 + dp[value - coin])

    if dp[total] == float('Infinity'):
        return -1
    return dp[total]
