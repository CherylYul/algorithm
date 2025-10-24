"""
Leet code 347: Top K Frequent Elements
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        sorted_hash_map = sorted(
            hash_map.items(), key=lambda item: item[1], reverse=True
        )
        return [key[0] for key in sorted_hash_map[:k]]
