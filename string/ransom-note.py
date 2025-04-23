"""
Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Solution: hash table
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        dictionary = {}
        for char in magazine:
            dictionary[char] = dictionary.get(char, 0) + 1
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        return True
