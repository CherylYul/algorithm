"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Technique: Recursion or backtracking
Time complexity: O(2^n), where n is the length of nums
Space complexity: O(n), for the depth of the recursion stack
"""


class Solution(object):
    def subsets(self, nums):
        def internal(nums, depth, curr, result, idx_min):
            if depth == len(nums):
                return
            curr = result[-1]
            for i in range(depth, len(nums)):
                if i > idx_min:
                    new_combo = curr[:]
                    new_combo.append(nums[i])
                    result.append(new_combo)
                    internal(nums, depth + 1, curr, result, i)

        result = [[]]
        internal(nums, 0, [], result, -1)
        return result
