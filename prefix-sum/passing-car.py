# O(N)
def solution(A):
    n = len(A)
    suffix = [0] * n
    suffix[n - 1] = A[n - 1]
    passing_cars = 0
    for i in range(n - 2, -1, -1):
        if A[i] == 0:
            suffix[i] = suffix[i + 1]
            passing_cars += suffix[i]
            if passing_cars > 1000000000:
                return -1
        else:
            suffix[i] = suffix[i + 1] + A[i]
    return passing_cars
