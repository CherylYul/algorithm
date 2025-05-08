"""
LeetCode 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
Time complexity: O(n)
Space complexity: O(n)
Techniques: Stack
"""


class Solution(object):
    def isValid(self, s):
        paren_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in paren_dict:
                stack.append(paren_dict[char])
            else:
                if len(stack) <= 0:
                    return False
                if char == stack[-1]:
                    stack.pop()
                    continue
                return False
        return len(stack) == 0
