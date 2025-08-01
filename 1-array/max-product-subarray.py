"""
Leet code 152: Maximum Product Subarray
Techniques: Prefix and Suffix Products
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        prefix, suffix, best = 1, 1, -float("inf")
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            best = max(best, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return best

    # Wrong Attempt: window sliding technique, it does not work for negative numbers from the right, 91% accepted
    # def maxProduct(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
    #     best, curr, prev_curr = -float("inf"), 1, None
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             best = max(best, nums[i])
    #             curr, prev_curr = 1, None
    #             continue
    #         curr *= nums[i]
    #         best = max(best, curr)
    #         if curr < 0:
    #             if not prev_curr:
    #                 prev_curr, curr = curr, 1
    #             else:
    #                 curr *= prev_curr
    #                 best = max(best, curr)
    #                 prev_curr = None
    #     return best
