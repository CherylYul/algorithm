"""
Leet code 836: Rectangle Overlap
Techniques: Math
Complexity: O(1)
Space Complexity: O(1)
"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if (
            rec2[2] <= rec1[0]
            or rec1[2] <= rec2[0]
            or rec2[3] <= rec1[1]
            or rec1[3] <= rec2[1]
        ):
            return False
        return True

    def isRectangleOverlap(self, rec1, rec2):
        width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return True if width > 0 and height > 0 else False
