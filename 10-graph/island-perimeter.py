"""
Leet code 463: Island Perimeter
Techniques: BFS, DFS, normal iteration
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * n) for the queue in BFS, O(1) for normal iteration
"""

from collections import deque


class Solution(object):
    def islandPerimeter(self, grid):
        row, col = len(grid), len(grid[0])
        p = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    p += 4
                    if r and grid[r - 1][c]:
                        p -= 2
                    if c and grid[r][c - 1]:
                        p -= 2
        return p

    def islandPerimeter(self, grid):
        row, col = len(grid), len(grid[0])
        q = deque([])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    q.append((r, c))
                    break
            if q:
                break
        p = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q:
            r, c = q.popleft()
            p += 4
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != 0:
                    p -= 1
                    if grid[nr][nc] != 2:
                        q.append((nr, nc))
                    grid[nr][nc] = 2
        return p
