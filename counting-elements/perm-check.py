# A permutation is a sequence containing each element from 1 to N once, and only once.
# O(N) or O(N * log(N))
# [4, 1, 3, 2] 1
# [4, 1, 3] 0


def solution(A):
    n = len(A)
    check = [False] * n
    for i in range(n):
        # if there is element larger than its length
        # if there are 2 same elements
        # if number < 0
        if A[i] > n or A[i] < 0 or check[A[i] - 1]:
            return 0
        check[A[i] - 1] = True
    return 1
