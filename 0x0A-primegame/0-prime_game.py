#!/usr/bin/python3
""" The Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing
        the number of elements in each round.

    Returns:
        str: The name of the winner ('Maria' or 'Ben')
        or None if there is no winner.

    """
    if x < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    for n in nums:
        primes_count = sum(primes[:n])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
