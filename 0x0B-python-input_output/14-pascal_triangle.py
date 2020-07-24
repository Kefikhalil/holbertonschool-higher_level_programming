#!/usr/bin/python3
"""Triangle class"""


def pascal_triangle(n):
    """Pascal triangle
    """
    if n <= 0:
        return []
    result = []
    last = []
    for x in range(n):
        row = []
        for i in range(x + 1):
            if x == 0 or i == 0 or x == j:
                row.append(1)
            else:
                row.append(last[i] + last[i - 1])
        last = row
        result.append(row)
    return result