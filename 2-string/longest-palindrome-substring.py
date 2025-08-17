"""
Leet code 5: Longest Palindrome Substring
Techniques: expand around center using two pointers
Time complexity: O(n^2)
Space complexity: O(1)
"""


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        longest = s[0]
        if s[0] == s[1]:
            longest = s[0:2]
        for i in range(1, len(s) - 1):
            s_odd = self.checkPalindromeLength(i - 1, i + 1, s)
            if len(longest) < len(s_odd):
                longest = s_odd
            if s[i] == s[i + 1]:
                s_even = self.checkPalindromeLength(i - 1, i + 2, s)
                if len(longest) < len(s_even):
                    longest = s_even
            if len(longest) > (len(s) - i) * 2:
                return longest
        return longest

    def checkPalindromeLength(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]
