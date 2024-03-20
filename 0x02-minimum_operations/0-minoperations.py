#!/usr/bin/python3
"""
This script defines a function to calculate the fewest number of operations needed
to achieve exactly n H characters in a file, given that the text editor can execute
only two operations: Copy All and Paste.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to achieve exactly n H characters in a file.

    Args:
        n (int): The target number of characters to achieve.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 0:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0

# Example usage
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

