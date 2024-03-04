# Island Perimeter

## Problem Description

Given a 2D grid representing a map of `1`s (land) and `0`s (water), compute the perimeter of the island. The island is surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

An island is defined as a group of adjacent cells horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

## Example
```
Input:
[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```
Output: 16

## Approach

To solve this problem, we can iterate over each cell in the grid and check if it is a land cell (`1`). If it is, we increment the perimeter by 4 and check its adjacent cells. If any adjacent cell is also a land cell, we decrement the perimeter by 1.

## Implementation
Here's the implementation of the `island_perimeter` function in Python:
```
from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
```
