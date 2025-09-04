"""
Leet code 1323: Maximum 69 Number
Techniques: String Manipulation
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def maximum69Number(self, num):
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == "6":
                s[i] = "9"
                break
        return int("".join(s))

    def maximum69Number(self, num):
        s = str(num)
        for i in range(0, len(s)):
            if s[i] == "6":
                return int(s[:i] + "9" + s[i + 1 :])
        return num
