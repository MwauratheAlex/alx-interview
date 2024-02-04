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
    dp = [float('inf') for i in range(total + 1)]
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    out = dp[amount]
    return out if out != float('inf') else -1
