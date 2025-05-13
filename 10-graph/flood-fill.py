"""
Leetcode 733. Flood Fill
An image is represented by an m x n integer grid image (0-indexed),
where each integer represents the pixel value of the image.
Time complexity: O(nxm)
Space complexity: O(nxm)
Techniques: BFS, Queue
"""

from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        r, c = len(image), len(image[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        visited = set()
        q = deque([(sr, sc)])
        fill_color = image[sr][sc]
        while q:
            x, y = q.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                image[x][y] = color
                for direction in directions:
                    next_r, next_c = x + direction[0], y + direction[1]
                    if (
                        0 <= next_r < r
                        and 0 <= next_c < c
                        and image[next_r][next_c] == fill_color
                    ):
                        q.append((next_r, next_c))
        return image
