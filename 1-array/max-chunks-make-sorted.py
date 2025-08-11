"""
Leet code 769: Max Chunks To Make Sorted
Techniques: max so far, prefix sum, monotonic stack
Complexity: O(n) for all approaches
Space Complexity: O(1) for max so far and prefix sum, O(n) for monotonic stack
"""


class Solution(object):
    def maxChunksToSorted(self, arr):
        chunks, max_pos = 1, arr[0]
        for i in range(1, len(arr)):
            if i > max_pos:
                chunks += 1
            max_pos = max(max_pos, arr[i])
            if max_pos == len(arr) - 1:
                return chunks
        return chunks

    def maxChunksToSorted(self, arr):
        curr_sum, exp_sum, chunks = 0, 0, 0
        for i in range(0, len(arr)):
            curr_sum += arr[i]
            exp_sum += i
            if curr_sum == exp_sum:
                chunks += 1
        return chunks

    def maxChunksToSorted(self, arr):
        s = []
        for i in range(len(arr)):
            val = arr[i]
            while len(s) > 0 and s[-1] > arr[i]:
                val = max(val, s[-1])
                s.pop()
            s.append(val)
        return len(s)
