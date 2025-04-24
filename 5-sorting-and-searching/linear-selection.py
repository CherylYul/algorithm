"""
Given an array A of n distinct numbers, find the k-th smallest one.
1. Choose pivot: try to choose the approximate median value
2. Construct the lhs which smaller than pivot, and rhs which larger than pivot

O(N)
"""
import math
from random import shuffle
import random


def select(a, k):

    # base case
    if len(a) <= 50:
        a = merge_sort(a)
        return a[k - 1]

    # choose pivot
    pivot = choose_pivot(a, len(a))

    # partition
    lhs = []
    rhs = []
    for i in range(len(a)):
        if i == pivot:
            continue
        if a[i] < pivot:
            lhs.append(a[i])
        else:
            rhs.append(a[i])

    if len(lhs) == k - 1:
        return pivot
    elif len(lhs) > k - 1:
        return select(lhs, k)
    elif len(lhs) < k - 1:
        return select(rhs, k - len(lhs) - 1)


def choose_pivot(a, n):
    g = int(math.ceil(n / 5))
    pivot = [[] for _ in range(g)]
    c = []
    for i in range(g - 1):
        pivot[i] = merge_sort(a[i : i + 5])
        c.append(pivot[i][2])
    pivot[g - 1] = merge_sort(a[i + 5 :])
    c.append(pivot[g - 1][len(pivot[g - 1]) // 2])
    p = select(c, g / 2)
    return p


"""
Choose pivot choice: from lecture 4 CS161 winter 2022
"""

# O(1)
def chooseRandomPivot(a):
    return random.choice(range(len(a)))


# O(1)
def chooseArbitraryPivot(a):
    return round(len(a) / 2)


# O(1)
def chooseMyFavoritePivot(a, t=3):
    if len(a) < t + 1:
        return 0
    return t


# O(n log(n))
def chooseIdealPivot(a):
    b = a[:]
    b.sort()
    pivotVal = b[(len(b) / 2).__trunc__()]
    return a.index(pivotVal)


# O(n)
def chooseWorstPivot(A):
    m = min(A)
    return A.index(m)


def merge_sort(a, depth=0):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(
        merge_sort(a[:mid], depth + 1), merge_sort(a[mid:], depth + 1), depth + 1
    )


def merge(a1, a2, depth=0):
    a, i, j = [], 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            a.append(a1[i])
            i += 1
        else:
            a.append(a2[j])
            j += 1
    return a + a1[i:] + a2[j:]


A = list(range(1, 100))
shuffle(A)
print(A)
print("The 2'th smallest is", select(A, 2))
print("The 73'th smallest is", select(A, 73))
print("The 17'th smallest is", select(A, 17))
