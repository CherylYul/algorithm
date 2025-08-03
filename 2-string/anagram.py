"""
Leet code 242: Valid Anagram
Given two strings s and t, return true if t is an anagram of s.
Techniques: Counter
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counter_s = [0] * 26
        counter_t = [0] * 26
        for i in range(len(s)):
            counter_s[ord(s[i]) - ord("a")] += 1
            counter_t[ord(t[i]) - ord("a")] += 1
        return counter_s == counter_t
