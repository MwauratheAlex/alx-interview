#!/usr/bin/env python3
# Return: fewest number of coins needed to meet total
# If total is 0 or less, return 0
# If total cannot be met by any number of coins you have, return -1
def makeChange(coins, total):
    dp = [float('Infinity')] * (total + 1)
    dp[0] = 0

    for value in range(1, len(dp)):
        for coin in coins:
            if coin > value:
                continue
            dp[value] = min(dp[value], 1 + dp[value - coin])

    if dp[total] == float('Infinity'):
        return -1
    return dp[total]
