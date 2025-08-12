"""
Leet code 200: Number of Islands
Techniques: BFS, DFS
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * n) for visited set
"""

from collections import deque


class Solution(object):
    # DFS
    def numIslands(self, grid):
        row, col = len(grid), len(grid[0])

        def traverse(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            traverse(r + 1, c)
            traverse(r - 1, c)
            traverse(r, c + 1)
            traverse(r, c - 1)

        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                    traverse(r, c)
        return count

    # BFS
    def numIslands(self, grid):
        row, col = len(grid), len(grid[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(r, c):
            q = deque([(r, c)])
            while q:
                i, j = q.popleft()
                if (i, j) not in visited:
                    visited.add((i, j))
                    for d in directions:
                        next_r, next_c = i + d[0], j + d[1]
                        if (
                            0 <= next_r < row
                            and 0 <= next_c < col
                            and grid[next_r][next_c] == "1"
                        ):
                            q.append((next_r, next_c))

        count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == "1":
                    count += 1
                    traverse(r, c)
        return count
