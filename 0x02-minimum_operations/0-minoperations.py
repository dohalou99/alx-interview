#!/usr/bin/python3
'''A Coding challenge.
'''
def minOperations(n):
"""
    Determines the fewest number of operations
    needed to achieve exactly n H characters in a file.

    Args:
        n (int): Number of characters to be achieved.

    Returns:
        int: The minimum number of operations required.
    """

    now = 1  # Current number of characters in the file
    start = 0  # Starting number of characters for each round of operations
    counter = 0  # Total number of operations

    while now < n:
        remainder = n - now

        # Check if the remainder is divisible by the current number of characters
        if remainder % now == 0:
            start = now
            now += start
            counter += 2  # Copy all and paste operations
        else:
            now += start
            counter += 1  # Only paste operation

    return counter
