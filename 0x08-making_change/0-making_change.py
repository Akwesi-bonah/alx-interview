#!/usr/bin/python3
""" modul make chage"""

from typing import List


def makeChange(coins, total) -> int:
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    coins_count = 0
    sorted_coins = sorted(coins, reverse=True)
    for coin in sorted_coins:
        if total >= coin:
            coins_count += total // coin
            total %= coin
    return coins_count if total == 0 else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
