"""
Leet Code 389: Find the Difference
Technique: Hash Map, ASCII Sum, Bit Manipulation, Sorting
Complexity: O(n) for the hash map or ASCII sum, O(n log n) for sorting
Space Complexity: O(n) for the hash map, O(1) for ASCII sum
"""


class Solution(object):
    # hash map
    def findTheDifference(self, s, t):
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) - 1
            hash_map[t[i]] = hash_map.get(t[i], 0) + 1
        hash_map[t[len(t) - 1]] = hash_map.get(t[len(t) - 1], 0) + 1
        for char in hash_map:
            if hash_map[char] > 0:
                return char

    # ASCII sum
    def findTheDifference(self, s, t):
        total = 0
        for char in s:
            total -= ord(char)
        for char in t:
            total += ord(char)
        return chr(total)

    # bit manipulation
    def findTheDifference(self, s, t):
        charNo = 0
        for i in range(len(s)):
            charNo ^= ord(s[i]) ^ ord(t[i])
        charNo ^= ord(t[len(t) - 1])
        return chr(charNo)
