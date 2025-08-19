"""
Leet code 130: Surrounded Regions
Techniques: BFS, DFS
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * n) for the queue in BFS, O(m * n) for the visited set in DFS
"""

from collections import deque


class Solution(object):
    # DFS
    def solve(self, board):
        row, col = len(board), len(board[0])
        if row < 3 or col < 3:
            return
        grid = [["X" for _ in range(col)] for _ in range(row)]

        def traverse(r, c):
            if (
                r < 0
                or c < 0
                or r >= row
                or c >= col
                or board[r][c] == "X"
                or grid[r][c] == "O"
            ):
                return
            grid[r][c] = "O"
            traverse(r - 1, c)
            traverse(r + 1, c)
            traverse(r, c - 1)
            traverse(r, c + 1)

        for r in range(1, row - 1):
            if board[r][0] == "O":
                traverse(r, 0)
            if board[r][col - 1] == "O":
                traverse(r, col - 1)

        for c in range(1, col - 1):
            if board[0][c] == "O":
                traverse(0, c)
            if board[row - 1][c] == "O":
                traverse(row - 1, c)

        for r in range(1, row - 1):
            for c in range(1, col - 1):
                if board[r][c] != grid[r][c]:
                    board[r][c] = grid[r][c]

    # BFS
    def solve(self, board):
        row, col = len(board), len(board[0])
        if row < 3 or col < 3:
            return
        grid = [["X" for _ in range(col)] for _ in range(row)]

        def traverse(r, c):
            q = deque([(r, c)])
            while q:
                i, j = q.popleft()
                if (
                    0 <= i < row
                    and 0 <= j < col
                    and board[i][j] == "O"
                    and grid[i][j] != "O"
                ):
                    grid[i][j] = "O"
                    q.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        for r in range(1, row - 1):
            if board[r][0] == "O":
                traverse(r, 0)
            if board[r][col - 1] == "O":
                traverse(r, col - 1)

        for c in range(1, col - 1):
            if board[0][c] == "O":
                traverse(0, c)
            if board[row - 1][c] == "O":
                traverse(row - 1, c)

        for r in range(1, row - 1):
            for c in range(1, col - 1):
                if board[r][c] != grid[r][c]:
                    board[r][c] = grid[r][c]
