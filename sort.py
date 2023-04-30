import random


def selectionSort(A):
    B = [None for i in range(len(A))]
    for x in A:
        for i in range(len(B)):
            if B[i] == None or B[i] > x:
                j = len(B) - 1
                while j > i:
                    B[j] = B[j - 1]
                    j -= 1
                B[i] = x
                break
    return B


def insertionSort(a):
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and a[j] > current:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a


def mergeSort(a, depth=0):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(
        mergeSort(a[:mid], depth + 1), mergeSort(a[mid:], depth + 1), depth + 1
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


A = [5, 3, 4, 1, 6]
print(selectionSort(A))
print(insertionSort(A))
A = [5, 4, 1, 8, 7, 2, 6, 3]

input = list(range(1000))
output = list(range(1000))
random.shuffle(input)

print(mergeSort(A))
