"""
Leet Code 217: Contains Duplicate
Techniques: set, sort, check length
Complexity: O(n) where n is the length of nums
Space: O(n)
"""


class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
