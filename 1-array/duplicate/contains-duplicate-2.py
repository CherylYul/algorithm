"""
Leet code 219: Contains Duplicate II
Techniques: Hash Map
Complexity: O(n) where n is the length of nums
Space Complexity: O(n) for the hash map
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map and i - hash_map[nums[i]] <= k:
                return True
            hash_map[nums[i]] = i
        return False
