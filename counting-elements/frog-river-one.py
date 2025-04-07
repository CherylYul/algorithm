# Find the earliest time when a frog can jump to the other side of a river.
# (5, [1, 3, 1, 4, 2, 3, 5, 4]) 6
# (5, [5, 5, 5, 1, 1, 4, 2, 2]) -1
# Time Complexity: O(N)


def solution(X, A):
    n = len(A)
    num_of_leaf = 0
    leaf = [False] * (X + 1)
    for i in range(n):
        if not leaf[A[i]]:
            leaf[A[i]] = True
            num_of_leaf += 1
            if num_of_leaf == X:
                return i
    return -1
