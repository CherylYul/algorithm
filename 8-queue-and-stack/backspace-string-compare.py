"""
Leet code 844: Backspace String Compare
Techniques: two pointers, stack
Complexity: O(n) for both approaches where n is the length of the longer string
Space Complexity: O(1) for two pointers, O(n) for stack
"""


class Solution(object):
    # two pointers (tricky with many edge cases)
    def backspaceCompare(self, s, t):
        sp, tp = len(s) - 1, len(t) - 1
        while sp >= 0 or tp >= 0:
            skip_s = skip_t = 0
            while sp >= 0 and (skip_s or s[sp] == "#"):
                skip_s = skip_s + 1 if s[sp] == "#" else skip_s - 1
                sp -= 1
            while tp >= 0 and (skip_t or t[tp] == "#"):
                skip_t = skip_t + 1 if t[tp] == "#" else skip_t - 1
                tp -= 1
            if sp >= 0 and tp >= 0 and s[sp] != t[tp]:
                return False
            sp -= 1
            tp -= 1
        return False if sp != tp else True

    # stack
    def backspaceCompare(self, s, t):
        def streamStr(input):
            stack = []
            for char in input:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return streamStr(s) == streamStr(t)
