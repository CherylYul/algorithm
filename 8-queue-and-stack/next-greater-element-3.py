"""
Leet code 556: Next Greater Element III
Techniques: two pointers
Complexity: O(n) where n is the number of digits in n
Space Complexity: O(n) for the stack used to store digits
"""


class Solution(object):
    def nextGreaterElement(self, n):
        s, div = [], 10
        res = 0
        while n:
            s.append(n % div)
            n /= 10
        pointer, i = 0, 1
        while i < len(s) and s[i] >= s[i - 1]:
            i += 1
        if i >= len(s):
            return -1
        while s[i] >= s[pointer]:
            pointer += 1
        s[i], s[pointer] = s[pointer], s[i]
        for j in range(len(s) - 1, i - 1, -1):
            res = res * 10 + s[j]
        for j in range(0, i):
            res = res * 10 + s[j]
        return res if res < 2**31 else -1
