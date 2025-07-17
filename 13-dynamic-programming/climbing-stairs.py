"""
Solution: dynamic programming with memoization, or recursion with caching.
Time Complexity: O(n), where n is the number of steps.
Space Complexity: O(n), for the cache array.
"""


class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        cache = [0] * (n + 1)
        cache[1] = 1
        cache[2] = 2

        def recursion(n):
            if cache[n] != 0:
                return cache[n]
            cache[n] = recursion(n - 2) + recursion(n - 1)
            return cache[n]

        recursion(n)
        return cache[n]

    def climbStairs2(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
