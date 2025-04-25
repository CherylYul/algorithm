"""
if an element is 0, set its entire row and column to 0's.
1 1 1    1 0 1
1 0 1 -> 0 0 0
1 1 1    1 0 1

Time Complexity: O(N * M)
Space Complexity: O(N + M)
Most optimal solution is to use O(1) space:
use first row and first column in the matrix as markers
"""


class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return []
        row_l = len(matrix)
        col_l = len(matrix[0])
        row = [False] * row_l
        col = [False] * col_l

        for i in range(row_l):
            for j in range(col_l):
                if matrix[i][j] == 0:
                    row[i], col[j] = True, True

        for i in range(row_l):
            if row[i]:
                matrix[i] = [0] * col_l

        for j in range(col_l):
            if col[j]:
                for i in range(row_l):
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        if not matrix:
            return []
        r = len(matrix)
        c = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, r):
            for j in range(1, c):
                matrix[i][j] = (
                    0 if matrix[0][j] == 0 or matrix[i][0] == 0 else matrix[i][j]
                )

        if first_row_zero:
            for j in range(c):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(r):
                matrix[i][0] = 0
