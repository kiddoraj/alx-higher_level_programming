#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
