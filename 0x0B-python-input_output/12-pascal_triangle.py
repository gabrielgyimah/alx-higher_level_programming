#!/usr/bin/python3

"""Pascal Triangle Module/ Function"""


def pascal_triangle(n):
    """
    1. Prints Pascal Triangle
    2. Returns an empty list if n <= 0
    3. can assume n will be always an integer
    4. not allowed to import any module
    """
    if n <= 0:
        return []

    ans = [[1]]

    for _ in range(n - 1):
        tmp = [0] + ans[-1] + [0]
        row = []

        for j in range(len(ans[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        ans.append(row)

    return ans
