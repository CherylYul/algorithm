"""
Leet Code 704: Binary Search
Technique: Binary Search
Complexity: O(log n) for the binary search
Space Complexity: O(1)
"""


class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
