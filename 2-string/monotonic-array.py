"""
Leet code 896: Monotonic Array
Techniques: two pointers, linear scan
Complexity: O(n) where n is the length of the array
Space Complexity: O(1)
"""


class Solution(object):
    def isMonotonic(self, nums):
        if len(nums) == 1:
            return True
        if nums[-1] > nums[0]:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
        elif nums[-1] < nums[0]:
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i] != nums[0]:
                    return False
        return True
