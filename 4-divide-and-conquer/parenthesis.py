"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution(object):
    def generateParenthesis(self, n):
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")

        res = []
        dfs(0, 0, "")
        return res
