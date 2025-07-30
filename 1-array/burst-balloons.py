"""
LeetCode 452. Minimum Number of Arrows to Burst Balloons
Technique: Sorting
Time Complexity: O(n log n)
Space Complexity: O(1)
"""


class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        arrow = 1
        overlap = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > overlap:
                arrow += 1
                overlap = points[i][1]
            else:
                overlap = min(points[i][1], overlap)
        return arrow
