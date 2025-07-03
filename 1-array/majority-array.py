"""
Solution1: counter
Time complexity: O(n)
Space complexity: O(n)

Solution2: sorting and return the middle element
Time complexity: O(n log n)
Space complexity: O(1)

Solution3: Boyer-Moore Voting Algorithm
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        best_key = 0
        best = 0
        for key in counter:
            if counter[key] > best:
                best = counter[key]
                best_key = key

        return best_key

    def majorityElement2(self, nums):
        mid = len(nums) // 2
        nums = sorted(nums)
        return nums[mid]
