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

    if(n > 0):
        pascal_list = [[1]]
        for line in range(n - 1):
            row_above = [0] + pascal_list[-1] + [0]
            row_below = []
            for i in range(len(row_above) - 1):
                row_below.append(row_above[i] + row_above[i + 1])
            pascal_list.append(row_below)
        return(pascal_list)
    return(pascal_list)

if __name__ == "__main__":
    pascal_triangle()


"""    pascal_list = []

    if(n > 0):
        for line in range(1, n + 1):
            row_list = []
            C = 1
            for i in range(1, line + 1):
                row_list.append(C)
                print(row_list, i)
                print("new")
                C = int(C * (line - i) / i)
            pascal_list.append(row_list)
        return(pascal_list)
    return(pascal_list)
    Runs with error at n = 63
    """
