"""
Leet code 169: Majority Element
Techniques: Hash Map, Sorting, Boyer-Moore Voting Algorithm, Bit Manipulation, Divide and Conquer, Randomization (6 solutions)
Complexity: O(n) where n is the length of nums, O(n log n) for sorting
Space Complexity: O(n) for the hash map, O(1) for sorting and Boyer-Moore Voting Algorithm
"""


class Solution(object):
    # Hash Map
    def majorityElement(self, nums):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] > len(nums) / 2:
                return num

    # Sorting
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) / 2]

    # Boyer-Moore Voting Algorithm
    def majorityElement(self, nums):
        count, majority = 1, nums[0]
        for i in range(1, len(nums)):
            if count == 0 and nums[i] != majority:
                count, majority = 1, nums[i]
            elif nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority
