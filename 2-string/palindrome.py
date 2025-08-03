"""
Leet code 125: Valid Palindrome
Techniques: string manipulation, regex
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        s_strip = "".join(char.lower() for char in s if char.isalnum())
        return s_strip == s_strip[::-1]
