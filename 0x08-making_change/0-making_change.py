#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins: list, total: int) -> int:
    """
    method to determine the fewest number of coins
    in a list needed to meet a given total
    """
    minCoins = [float('inf')] * (total + 1)

    minCoins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return minCoins[total] if minCoins[total] != float('inf') else -1
