"""
Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] total combinations = 6
Technique: Recursion or backtracking
Time complexity: O(C(n^k)), each valid combination generated once
Space complexity: O(k) for single curr array
"""


class Solution(object):
    def combine(self, n, k):
        def comb(n, k, depth, curr, result):
            if depth == k:
                result.append(curr[:])
                return
            for i in range(depth, n - (k - depth) + 1):
                add_new = i + 1
                if depth == 0 or add_new > curr[depth - 1]:
                    curr[depth] = add_new
                    comb(n, k, depth + 1, curr, result)

        result = []
        curr = [0] * k
        comb(n, k, 0, curr, result)
        return result

    # use stack: slower
    def combine2(self, n, k):
        if k == 0:
            return [[]]

        result = []
        stack = [[]]

        while stack:
            current = stack.pop()
            start = current[-1] + 1 if current else 1

            for i in range(start, n + 1):
                new_combo = current + [i]
                if len(new_combo) == k:
                    result.append(new_combo)
                else:
                    stack.append(new_combo)

        return result
