#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    matrix = []

    if n <= 0:
        return matrix

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        matrix.append(row)
    return matrix


if __name__ == "__main__":

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
