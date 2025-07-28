"""
LeetCode 416. Partition Equal Subset Sum
Techniques: Dynamic Programming, Set
Time complexity: O(n * sum(nums))
Space complexity: O(sum(nums))
"""


class Solution(object):
    def canPartitionWithSet(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2
        dp = set([0])
        for num in nums:
            next_sums = set()
            for v in dp:
                if v + num == target:
                    return True
                next_sums.add(v + num)
                next_sums.add(v)
            dp = next_sums
            print(dp)
        return target in dp

    def canPartitionWithDp(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for curr in range(target, num - 1, -1):
                dp[curr] = dp[curr] or dp[curr - num]
        return dp[target]
