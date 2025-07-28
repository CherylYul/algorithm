"""
Leet code 198. House Robbery
Solution: Dynamic Programming
Time Complexity: O(n), where n is the number of houses.
Space Complexity: O(1), since we only need to keep track of the last two results
"""


class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        # no need to store dp, only need some prev values
        prev, best = nums[0], nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2, len(nums)):
            temp = best
            best = max(nums[i] + prev, best)
            prev = temp
        return best
