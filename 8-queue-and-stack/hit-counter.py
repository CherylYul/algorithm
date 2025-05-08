"""
LeetCode 362. Design Hit Counter
Design a hit counter which counts the number of hits received in the past 5 minutes.
Time complexity: O(log n) for getHits, O(1) for hit
Space complexity: O(n) for storing the hits
Techniques: Binary Search
"""


class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        left, right = 0, len(self.hits) - 1
        target = timestamp - 300
        while left <= right:
            mid = (left + right) // 2
            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return len(self.hits) - left
