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
    change = 0
    coins.sort(reverse=True)
    for coin in coins:
        if total == 0:
            break
        tmp = total // coin
        change += tmp
        total -= (tmp * coin)

    return -1 if total != 0 else change
