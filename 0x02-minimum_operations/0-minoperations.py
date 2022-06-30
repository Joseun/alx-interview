#!/usr/bin/python3
""" a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file. """


def minOperations(n: int) -> int:
    """
    write a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Argument:
    n: integer
    """
    if n == 1:
        return 0
    if n <= 5:
        return n
    for i in range(n//2, -1, -1):
        if n % i == 0:
            return minOperations(i) + (n // i)

if __name__ == "__main__":
    minOperations()
