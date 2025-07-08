"""
Return True if the array contains any duplicates.
Solution: Use a set to track seen elements.
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False
