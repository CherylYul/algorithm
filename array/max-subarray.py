"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Solution: sliding window
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def maxSubArray(self, nums):
        curr, max_sum = 0, nums[0]
        for i in range(len(nums)):
            curr += nums[i]
            max_sum = max(curr, max_sum)
            if curr < 0:
                curr = 0
        return max_sum
