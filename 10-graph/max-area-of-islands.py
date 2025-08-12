"""
Leet Code 695: Max Area of Islands
Techniques: DFS, BFS
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(1) for DFS, O(m * n) for BFS
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        row, col, best = len(grid), len(grid[0]), 0

        def traverse(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return (
                1
                + traverse(r + 1, c)
                + traverse(r - 1, c)
                + traverse(r, c + 1)
                + traverse(r, c - 1)
            )

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    best = max(best, traverse(r, c))
        return best
