# A[2, 3, 7, 5, 1, 3, 9]
# k = 4, m = 6
# spot = 3 -> 2 -> 3 -> 4 -> 5 -> 6, collect 25 mushrooms


# O(n)
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P, x, y):
    return P[y + 1] - P[x]


def solution(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n, max(k, k + m - 2 * p))
        result = max(result, pref[right_pos] - pref[left_pos])
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, pref[right_pos] - pref[left_pos])
    return result
