## 2D Rotation

To rotate a 2D matrix, you can use the following algorithm:

1. Create a new matrix of the same size as the original matrix.
2. Iterate through each element in the original matrix.
3. Calculate the new coordinates of the element after rotation.
4. Assign the value of the original element to the corresponding position in the new matrix.
5. Repeat steps 3-4 for all elements in the original matrix.
6. The new matrix will be the rotated version of the original matrix.

Here is an example implementation in Python:

```python
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

```
Output
```
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]

