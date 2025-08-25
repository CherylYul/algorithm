"""
Leet code 402: Remove K Digits
Techniques: monotonic stack
Complexity: O(n) where n is the length of num
Space Complexity: O(n) for the stack
"""


class Solution(object):
    # monotonic increasing stack
    def removeKdigits(self, num, k):
        s = []
        for d in num:
            while s and k and s[-1] > d:
                s.pop()
                k -= 1
            s.append(d)
        s = s[: len(s) - k]
        ans = "".join(s)
        return str(int(ans)) if ans else "0"

    # monotonic decreasing stack, time limit exceeded
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"
        ans, l, s = "", 0, []
        for i in range(len(num)):
            temp = []
            while s and num[s[-1]] <= num[i]:
                if s[-1] < l:
                    s.pop()
                else:
                    temp.append(s.pop())
            s.append(i)
            while temp:
                s.append(temp.pop())
            if i - l == k:
                min_pos = s.pop()
                ans += num[min_pos]
                k -= min_pos - l
                l = min_pos + 1
                if not k:
                    return str(int(ans + num[l:]))
        return str(int(ans))
