#!/usr/bin/python3
"""This module contains the function makeChange(coins, amount)"""


def makeChange(coins, total):
    """determines the fewest number of coins
    needed to meet a given amount total

    Args:
      coins: (int[]) array of coins
      total: (int) amout to get change for
    Returns: fewest coins to make total
    """
    if total <= 0:
        return 0
    dp = [[float('inf')] * (total + 1)] * (len(coins) + 1)
    for i in range(len(coins) + 1):
        for j in range(total + 1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = float('inf')
            elif coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])

    out = dp[len(coins)][total]
    return -1 if out == float('inf') else out
