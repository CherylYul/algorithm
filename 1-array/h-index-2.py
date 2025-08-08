"""
Leet Code 275: H-Index II
Technique: Binary Search
Complexity: O(log n) for the binary search
Space Complexity: O(1)
"""


class Solution(object):
    def hIndex(self, citations):
        l, r = 0, len(citations) - 1
        hIndex = 0
        while r >= l:
            mid = (l + r) / 2
            if len(citations) - mid == citations[mid]:
                return citations[mid]
            if len(citations) - mid < citations[mid]:
                hIndex = max(hIndex, len(citations) - mid)
                r = mid - 1
            else:
                hIndex = max(hIndex, citations[mid])
                l = mid + 1
        return hIndex
