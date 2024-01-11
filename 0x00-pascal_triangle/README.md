# Task: Pascal Triangle

## Description
The Pascal triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

## Implementation
To generate the Pascal triangle, we can use a nested loop. The outer loop iterates over the rows, and the inner loop iterates over the columns. We start with the first row, which contains only one element (1). Then, for each subsequent row, we calculate the values based on the previous row.

Here's an example implementation in Python:
```
def generate_pascal_triangle(num_rows):
    triangle = []
    for row in range(num_rows):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                previous_row = triangle[row - 1]
                current_row.append(previous_row[col - 1] + previous_row[col])
        triangle.append(current_row)
    return triangle

# Example usage
num_rows = 5
pascal_triangle = generate_pascal_triangle(num_rows)
for row in pascal_triangle:
    print(row)

## output
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```