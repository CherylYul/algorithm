"""
Leet code 300. Longest Increasing Subsequence
Solution: Dynamic Programming, binary search
Time Complexity: O(n^2) for DP, O(n log n) for binary search
Space Complexity: O(n) for DP, O(n) for binary search
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
