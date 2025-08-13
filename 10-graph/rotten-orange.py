"""
Leet code 994: Rotting Oranges
Techniques: BFS
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * n) for the queue
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        have_orange = 0
        rotten_orange = []
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
        minute = 0
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
            if next_time != []:
                minute += 1
                q.append(next_time)
        if rotten_nums < have_orange:
            return -1
        return minute
