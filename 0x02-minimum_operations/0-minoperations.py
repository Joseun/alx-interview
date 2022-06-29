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
    count = 0
    for i in range(2, n + 1):
        # check if problem can be broken into smaller problem
        while not n % i:
            # if yes then add no of smaller problems to result.
            count += i
            # create smaller problem
            n = n / i
    return count


if __name__ == "__main__":
    minOperations()
