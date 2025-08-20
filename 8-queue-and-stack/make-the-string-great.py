"""
Leet code 1544: Make The String Great
Techniques: Stack
Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the stack used to store characters
"""


class Solution(object):
    def makeGood(self, s):
        if len(s) < 2:
            return s
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
