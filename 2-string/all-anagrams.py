"""
Leet code 438: Find All Anagrams in a String
Techniques: sliding window, hash map
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        table = {}
        for char in p:
            table[char] = table.get(char, 0) + 1
        hash_map, count, l = table.copy(), 0, -1
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] -= 1
                count += 1
                while hash_map[s[i]] < 0:
                    l += 1
                    hash_map[s[l]] += 1
                    count -= 1
                if count == len(p):
                    res.append(i - len(p) + 1)
            else:
                hash_map, l, count = table.copy(), i, 0
            print(hash_map, count, l, res)
        return res
