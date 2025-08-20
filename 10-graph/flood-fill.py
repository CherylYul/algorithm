"""
Leet code 733: Flood Fill
Techniques: BFS, DFS
Complexity: O(m * n) where m is the number of rows and n is the number of columns
Space Complexity: O(m * n) for the queue in BFS, O(m * n) for the stack in DFS
"""

from collections import deque


class Solution(object):
    # BFS
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]
        image[sr][sc] = color
        q = deque([(sr, sc)])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q:
            r, c = q.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == original_color:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image

    # DFS
    def floodFill(self, image, sr, sc, color):
        if color == image[sr][sc]:
            return image
        row, col = len(image), len(image[0])
        origin_color = image[sr][sc]
        s = [(sr, sc)]
        while s:
            r, c = s.pop()
            if r < 0 or c < 0 or r >= row or c >= col or image[r][c] != origin_color:
                continue
            image[r][c] = color
            s.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
        return image
