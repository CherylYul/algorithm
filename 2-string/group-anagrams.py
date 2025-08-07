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


class Solution(object):
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
