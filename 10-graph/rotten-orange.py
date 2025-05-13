"""
Leetcode 994. Rotting Oranges
In a given grid, each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
Time complexity: O(nxm)
Space complexity: O(nxm)
Techniques: BFS, Queue
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        have_orange, rotten_orange = 0, []
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    have_orange += 1
                if grid[r][c] == 2:
                    rotten_orange.append((r, c))
        rotten_nums = len(rotten_orange)
        if have_orange == 0 or rotten_nums == have_orange:
            return 0
        if rotten_nums == 0:
            return -1
        time = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = deque([rotten_orange])
        while q:
            this_time = q.popleft()
            next_time = []
            for r, c in this_time:
                for d in directions:
                    next_r, next_c = r + d[0], c + d[1]
                    if (
                        0 <= next_r < row
                        and 0 <= next_c < col
                        and grid[next_r][next_c] == 1
                    ):
                        rotten_nums += 1
                        grid[next_r][next_c] = 2
                        next_time.append((next_r, next_c))
            time += 1
            if next_time != []:
                q.append(next_time)
        if rotten_nums < have_orange:
            return -1
        return time - 1
