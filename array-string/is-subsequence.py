"""
A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).
Example: Input: s = "abc", t = "ahbgdc" => Output: true
"""


class Solution(object):
    def isSubsequence(self, s, t):
        s_pt, t_pt = 0, 0
        s_len = len(s)
        t_len = len(t)
        while s_pt < s_len and t_pt < t_len:
            if s[s_pt] == t[t_pt]:
                s_pt += 1
            t_pt += 1

        if s_pt >= s_len:
            return True
        if t_pt >= t_len:
            return False
