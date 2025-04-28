"""
Given an m x n matrix, return all elements of the matrix in spiral order.
1 2 3 4
5 6 7 8
9 8 9 2
=> 1 2 3 4 8 2 9 8 9 5 6 7
"""


class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])  # r, c
        if m == 1:
            return matrix[0]

        r, c = 1, 0
        res = matrix[0]
        direction = "d"

        while r < m and c < n:
            if direction == "d":
                for i in range(r, m):
                    res.append(matrix[i][n - 1])
                direction = "l"
                n -= 1
                continue
            if direction == "l":
                for i in range(n - 1, c - 1, -1):
                    res.append(matrix[m - 1][i])
                direction = "u"
                m -= 1
                continue
            if direction == "u":
                for i in range(m - 1, r - 1, -1):
                    res.append(matrix[i][c])
                direction = "r"
                c += 1
                continue
            if direction == "r":
                for i in range(c, n):
                    res.append(matrix[r][i])
                direction = "d"
                r += 1
                continue
        return res
