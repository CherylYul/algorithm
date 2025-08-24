"""
Leet code 703: Kth Largest Element in a Stream
Techniques: Min Heap
Complexity: O(log k) for add operation, O(n) for the initial heapify
Space Complexity: O(k) for the heap used to store the k largest elements
"""

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
