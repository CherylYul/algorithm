"""
A permutation is a sequence containing each element from 1 to N once, and only once.
[4, 1, 3, 2] => 1 (True)
[4, 1, 3] => 0 (False)
Solution: counter
Time complexity: O(n)
Space complexity: O(n)
"""


def solution(A):
    n = len(A)
    check = [False] * n
    for i in range(n):
        # if there is element larger than its length
        # if number < 0
        # if there are 2 same elements
        if A[i] > n or A[i] < 0 or check[A[i] - 1]:
            return 0
        check[A[i] - 1] = True
    return 1
