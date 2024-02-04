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
    coin_count = 0
    rem = total
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    coin_idx = 0
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coin_count += 1
        else:
            coin_idx += 1
    return coin_count
