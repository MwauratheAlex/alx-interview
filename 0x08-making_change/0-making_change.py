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
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for a in range(total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != total + 1 else - 1
