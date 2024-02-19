#!/usr/bin/python3
"""
This returns a set of numbers that represent the Pascal Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    # Print the triangle for testing
    for row in triangle:
        print(row)

# Example usage:
pascal_triangle(5)
