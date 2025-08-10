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
