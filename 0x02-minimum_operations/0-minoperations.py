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
    dp = [0]*(n+1)
    if(n == 1): 
        return 0
    dp[1] = 0
    if(n == 2):
        return 2
    dp[2] = 2
    for i in range(3, n+1):
        max_fact = 1 if(i%2!=0) else 2
        if(max_fact!=2):
            for j in range(3,n//2,2):
                if(i%j==0):
                    max_fact = j
                    break
        dp[i] = dp[i//max_fact]+max_fact if max_fact!=1 else i
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
