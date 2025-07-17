"""
Leet code 322. Coin Change
Solution: Dynamic Programming
Time Complexity: O(n * amount)
Space Complexity: O(amount)
"""


class Solution(object):
    def coinChange(self, coins, amount):
        dp = [
            i / coins[0] if i % coins[0] == 0 else amount + 1 for i in range(amount + 1)
        ]
        for i in range(1, len(coins)):
            for val in range(coins[i], amount + 1):
                dp[val] = min(dp[val], 1 + dp[val - coins[i]])
        return -1 if dp[-1] > amount else dp[-1]
