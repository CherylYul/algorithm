"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
Solution: counter
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution(object):
    def createCounter(self, s):
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 0
        return counter

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counter_s = self.createCounter(s)
        counter_t = self.createCounter(t)
        for i in counter_s:
            if i not in counter_t:
                return False
            if counter_s[i] != counter_t[i]:
                return False
        return True

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        counter_s = [0] * 26
        counter_t = [0] * 26
        for i in range(len(s)):
            counter_s[ord(s[i]) - ord("a")] += 1
            counter_t[ord(t[i]) - ord("a")] += 1
        return counter_s == counter_t
