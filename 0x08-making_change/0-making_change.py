#!/usr/bin/python3
"""
makeChange Algorithm
"""
count = 0


def makeChange(coins, total):
    """ With a pile of coins of different values,
    return minimum number of coins needed to get a total amount.
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewest = count
    for coin in coins:
        if total <= 0:
            break
        buff = total // coin
        fewest += buff
        total -= (buff * coin)
    if total != 0:
        return -1
    return fewest