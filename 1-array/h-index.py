"""
Leet Code 274: H-Index
Technique: Sorting
Complexity: O(n log n) for sorting, O(n) for the loop
Space Complexity: O(1)
"""


class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        hIndex = 0
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                return len(citations) - i
            else:
                hIndex = citations[i]
        return hIndex
