# Coin Change Problem

The **Coin Change Problem** is a classic algorithmic problem in the field of dynamic programming. The goal is to determine the fewest number of coins needed to meet a given total amount using a pile of coins with different values.

## Problem Statement

Write a Python function `makeChange(coins, total)` that takes two parameters:

- `coins`: A list of values representing the different denominations of coins available.
- `total`: The target total amount for which you want to make change.

The function should return the fewest number of coins needed to meet the total amount. If the total is 0 or less, the function should return 0. If the total cannot be met by any combination of coins, the function should return -1.

## Example

```python
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)
```

Output:
```
3
```

In this example, we have coins with values [1, 2, 5], and we want to make change for the total amount of 11. The optimal solution is to use two coins with a value of 5 and one coin with a value of 1, resulting in a total of 11.

## Function Signature

```python
def makeChange(coins: List[int], total: int) -> int:
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


```

## Constraints

- The list of coin values (`coins`) will always contain integers greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.
- The function's runtime will be evaluated, so consider optimizing the solution.

## Edge Cases

- If `total` is 0 or less, the function should return 0.
- If the total cannot be met by any combination of coins, the function should return -1.

Feel free to include additional details, explanations, or optimizations in the readme.