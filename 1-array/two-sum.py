"""
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.
Solution: index as a hash key
O(n) time complexity and O(n) space complexity
"""


class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
