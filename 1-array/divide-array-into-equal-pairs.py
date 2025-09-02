"""
Leet Code 2206: Divide Array Into Equal Pairs
Techniques: hash map, set, bit manipulation
Time Complexity: O(n)
Space Complexity: O(n) for hash map and set, O(1) for bit manipulation
"""


class Solution(object):
    # hash map
    def divideArray(self, nums):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for key in hash_map:
            if hash_map[key] % 2 != 0:
                return False
        return True

    # set
    def divideArray(self, nums):
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return False if s else True

    # set, built-in function
    def divideArray(self, nums):
        for num in set(nums):
            if nums.count(num) % 2 != 0:
                return False
        return True

    # bit manipulation
    def divideArray(self, nums):
        k = 0
        for num in nums:
            k ^= 1 << num
        return k == 0
