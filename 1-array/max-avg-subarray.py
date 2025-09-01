"""
Leet code 643: Maximum Average Subarray I
Techniques: Sliding Window
Complexity: O(n) where n is the length of nums
Space Complexity: O(1)
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        curr = best = sum(nums[:k])
        for i in range(k, len(nums)):
            curr = curr + nums[i] - nums[i - k]
            best = max(curr, best)
        return float(best) / k
