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
    if n == 2:
        return 2
    dp = [float('inf')] * (n+1)  # dp[i] denote minimal operations for i 'A'
    # print(dp, '1')
    dp[1] = 0
    dp[2] = 2
    # print(dp, '2')
    for i in range(3, n+1):
        for j in range(1, (i//2)+1):
            # copy from anywhere when the number of missing 'A' (i-j)
            # is dividable by the number of existing 'A' (j)
            # the bottom line is when j == 1
            # 1 copy + (i-j)/j paste
            # print(i, j)
            if (i - j) % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 + (i-j)//j)
                # print(dp, '3')
    return dp[n]
    # count = 0
    # for i in range(2, n + 1):
    #     # check if problem can be broken into smaller problem
    #     while not n % i:
    #         # if yes then add no of smaller problems to result.
    #         count += i
    #         # create smaller problem
    #         n /= i
    # return count
