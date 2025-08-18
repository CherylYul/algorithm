"""
Leet code 496: Next Greater Element I
Techniques: Monotonic Stack, Hash Map
Complexity: O(n + m) where n is the length of nums1 and m is the length of nums2
Space Complexity: O(n) for the hash map

Leet code 503: Next Greater Element II
Techniques: Monotonic Stack two passes
Complexity: O(n) where n is the length of nums
Space Complexity: O(n) for the result array
"""


class Solution(object):
    # Next Greater Element I
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hash_map = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            hash_map[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = hash_map[nums1[i]]
        return nums1

    # Next Greater Element II
    def nextGreaterElements(self, nums):
        s, q = [], []
        res = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while s and nums[i] >= s[-1]:
                s.pop()
            res[i] = s[-1] if s else q.append(i)
            s.append(nums[i])
        for pos in q:
            while s and nums[pos] >= s[-1]:
                s.pop()
            res[pos] = s[-1] if s else -1
            s.append(nums[pos])
        return res
