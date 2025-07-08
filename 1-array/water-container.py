"""
Leet code 11
Solution 1: Brute Force Approach
Time Complexity: O(n^2)
Space Complexity: O(1)

Solution 2 : Two Pointer Approach
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def maxAreaBruteForce(self, height):
        best = 0
        for i in range(1, len(height)):
            for j in range(i):
                area = (i - j) * min(height[j], height[i])
                best = max(area, best)
        return best

    def maxAreaPointer(self, height):
        l, r, best = 0, len(height) - 1, 0
        while r > l:
            w = r - l
            h = height[l] if height[l] < height[r] else height[r]
            best = max(best, w * h)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return best
