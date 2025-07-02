"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.
Time complexity: O(n)
Space complexity: O(n)

Longest Palindrome:
Solution: counter
Time complexity: O(n)
Space complexity: O(n)
"""

import re


class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        s_strip = "".join(char.lower() for char in s if char.isalnum())
        return s_strip == s_strip[::-1]

    # using regex to remove non-alphanumeric characters
    def isPalindrome2(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return s == s[::-1]

    def longestPalindrome(self, s):
        if len(s) == 1:
            return 1
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        length = 0
        for char in s_dict:
            if s_dict[char] % 2 == 0:
                length += s_dict[char]
            else:
                length += s_dict[char] - 1
        return length + 1 if length < len(s) else length
