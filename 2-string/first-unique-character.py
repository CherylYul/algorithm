"""
Leet code 387: First Unique Character in a String
Techniques: Hash Map, 2 Sets, Counting, first last index
Complexity: O(n) where n is the length of the string
Space Complexity: O(1)
"""


class Solution(object):
    # first last index
    def firstUniqChar(self, s):
        for char in s:
            if s.rindex(char) == s.index(char):
                return s.index(char)
        return -1

    # counting
    def firstUniqChar(self, s):
        counter = [0] * 26
        for char in s:
            counter[ord(char) - 97] += 1
        for i in range(len(s)):
            if counter[ord(s[i]) - 97] == 1:
                return i
        return -1

    # 2 sets
    def firstUniqChar(self, s):
        unique, duplicates = set(), set()
        for char in s:
            if char in duplicates:
                continue
            elif char in unique:
                unique.remove(char)
                duplicates.add(char)
            else:
                unique.add(char)
        for i in range(len(s)):
            if s[i] in unique:
                return i
        return -1

    # hash map
    def firstUniqChar(self, s):
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1
