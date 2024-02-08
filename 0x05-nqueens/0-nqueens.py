#!/usr/bin/python3
"""Solution to the N-Queens puzzle"""
import sys


def print_board(board, n):
    """Prints allocated positions to the queen"""
    positions = []
    for i in range(n):
        for j in range(n):
            if j == board[i]:
                positions.append([i, j])
    print(positions)


def is_safe_position(board, row, col):
    """
    Determines whether the position is safe for the queen.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def find_queens_positions(board, row, n):
    """Recursively finds all safe positions where
      the queens can be allocated"""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if is_safe_position(board, row, col):
                board[row] = col
                find_queens_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0] * size


def solve_nqueens(n):
    """Solves the N-Queens puzzle"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(n)
    find_queens_positions(board, 0, n)


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
