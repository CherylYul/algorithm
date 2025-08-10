"""
Leet Code 378: Kth Smallest Element in a Sorted Matrix
Techniques: Binary Search, Min Heap, Merge Sort, BFS
Complexity: O(n log(max-min)) for binary search, O(k log n) for min heap, O(n^2 log n) for merge sort
Space Complexity: O(1) for binary search, O(n) for min heap, O(n^2) for merge sort
"""

import heapq


class Solution(object):
    # binary search, pointer
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            # print("start loop: ", l, r, mid)
            pointer = n - 1
            smaller_nums = 0
            for row in matrix:
                while pointer >= 0 and row[pointer] > mid:
                    pointer -= 1
                smaller_nums += pointer + 1
                # print("check pointer: ", pointer, smaller_nums)
            if smaller_nums >= k:
                r = mid
            else:
                l = mid + 1
        return l

    # min heap, BFS
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        visited = [[False for _ in range(n)] for _ in range(n)]
        min_heap = [(matrix[0][0], 0, 0)]
        k -= 1
        while min_heap:
            val, x, y = heapq.heappop(min_heap)
            if k == 0:
                return val
            visited[x][y] = True
            if x < n - 1 and not visited[x + 1][y]:
                heapq.heappush(min_heap, (matrix[x + 1][y], x + 1, y))
                visited[x + 1][y] = True
            if y < n - 1 and not visited[x][y + 1]:
                heapq.heappush(min_heap, (matrix[x][y + 1], x, y + 1))
                visited[x][y + 1] = True
            k -= 1

    # min heap
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(min_heap, matrix[i][j])
        for _ in range(k):
            k_element = heapq.heappop(min_heap)
        return k_element

    # merge sort
    def kthSmallest(self, matrix, k):
        if len(matrix) == 1 or k == 1:
            return matrix[0][0]
        if k == len(matrix) ** 2:
            return matrix[-1][-1]
        while len(matrix) > 1:
            temp = []
            for i in range(0, len(matrix), 2):
                l1 = matrix[i]
                l2 = matrix[i + 1] if i + 1 < len(matrix) else []
                temp.append(self.mergeLists(l1, l2))
            matrix = temp
        return matrix[0][k - 1]

    def mergeLists(self, l1, l2):
        new_list, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                new_list.append(l1[i])
                i += 1
            else:
                new_list.append(l2[j])
                j += 1
        return new_list + l1[i:] + l2[j:]
