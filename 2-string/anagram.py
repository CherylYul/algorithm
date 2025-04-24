class Solution(object):
    """
    Given two strings s and t, return true if t is an anagram of s,
    and false otherwise.
    Solution: counter
    Time complexity: O(n)
    Space complexity: O(n)
    """

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

    """
    2. Given an array of strings strs, group the anagrams together.
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Solution: hash table
    Time complexity: O(n * k)
    Space complexity: O(n * k)
    where n is the length of strs and k is the maximum length of a string 
    in strs.
    """

    def createKeys(self, string):
        counter = [""] * 26
        for char in string:
            counter[ord(char) - ord("a")] += char
        return "".join([el for el in counter])

    def groupAnagrams(self, strs):
        hash_table = {}
        for string in strs:
            hash_key = self.createKeys(string)
            if hash_key in hash_table:
                hash_table[hash_key].append(string)
            else:
                hash_table[hash_key] = [string]
        res = []
        for i in hash_table:
            res.append(hash_table[i])
        return res
