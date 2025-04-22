"""
Example: Input: s = "abc", t = "ahbgdc" => Output: true
solution: pointers
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
