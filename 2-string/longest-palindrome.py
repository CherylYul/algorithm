"""
Longest Palindrome:
Solution: counter
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution(object):
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
