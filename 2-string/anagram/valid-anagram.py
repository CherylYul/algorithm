"""
Leet code 242: Valid Anagram
Techniques: counter, hashmap, sort
Time: O(n)
Space: O(1)
"""


class Solution(object):
    # counter
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counter_s = [0] * 26
        counter_t = [0] * 26
        for i in range(len(s)):
            counter_s[ord(s[i]) - ord("a")] += 1
            counter_t[ord(t[i]) - ord("a")] += 1
        return counter_s == counter_t

    # hashmap
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
            hashmap[t[i]] = hashmap.get(t[i], 0) - 1
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True

    # sort
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
