"""
Leet code 238: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
Input: nums = [1,2,3,4] => [24,12,8,6]
Input: nums = [-1,1,0,-3,3] => [0,0,9,0,0]
Techniques: Prefix and Suffix Products
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res

    def productExceptSelf2(self, nums):
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        prevSuffix = 1
        for i in range(n - 2, -1, -1):
            prevSuffix *= nums[i + 1]
            res[i] *= prevSuffix

        return res
