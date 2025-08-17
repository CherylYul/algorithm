"""
Leet code 2696: Minimum String After Removing Substrings
Techniques: stack, greedy
Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack
"""


class Solution(object):
    def minLength(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] + char in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
