#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    method to determine the fewest number of coins
    from a list of coins needed to meet a given total
    """
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
