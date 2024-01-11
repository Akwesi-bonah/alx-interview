#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list of lists): A list of boxes,
        where each box is represented as a list of integers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
