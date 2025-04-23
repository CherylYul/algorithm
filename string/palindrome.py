"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and
numbers.
"""


class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        s_strip = "".join(char.lower() for char in s if char.isalnum())
        return s_strip == s_strip[::-1]
