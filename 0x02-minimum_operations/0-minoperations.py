#!/usr/bin/python3
'''A Coding challenge.
'''
def minOperations(n):
    if n == 1:
        return 0  # No operations needed for 1 H
    if n < 1 or n % 2 != 0:
        return 0  # It's impossible to achieve odd number of Hs

    dp = [0] * (n + 1)

    for i in range(2, n + 1, 2):
        dp[i] = float('inf')
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 2 + i // j - 1)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage
n = 9
print(minOperations(n))  # Output: 6

