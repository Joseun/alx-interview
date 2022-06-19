#!/usr/bin/python3
"""
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing
        the Pascal’s triangle of n

        Arguments:
            n: integer
    """

    pascal_list = []
    for line in range(1, n + 1):
        row_list = []
        C = 1
        for i in range(1, line + 1):
            row_list.append(C)
            C = int(C*(line - i)/i)
        pascal_list.append(row_list)
    return(pascal_list)

if __name__ == "__main__":
    pascal_triangle()
