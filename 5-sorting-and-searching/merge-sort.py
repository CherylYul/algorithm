import random

tests = []

tests.append(
    {
        "input": [5, 4, 1, 8, 7, 2, 6, 3],
        "output": [1, 2, 3, 4, 5, 6, 7, 8],
    }
)

tests.append(
    {
        "input": [6.9, 3.5, 5.5, 4.0, 4.1, 4.2, 6.3, 7.1],
        "output": [3.5, 4.0, 4.1, 4.2, 5.5, 6.3, 6.9, 7.1],
    }
)

tests.append(
    {
        "input": [9.9, 9.8, 9.4, 9.4, 9.4, 9.2, 9.1, 9.0, 8.9, 8.8, 8.8, 8.7],
        "output": [8.7, 8.8, 8.8, 8.9, 9.0, 9.1, 9.2, 9.4, 9.4, 9.4, 9.8, 9.9],
    }
)


"""
Merge sort divides the input into 2 parts, recursively solve the problem individually
each of the 2 parts, then combine the result solved the problem to original input

- Base case: the list is empty or only contains 1 element, return it
- Divide: divide the list into 2 roughly equal smaller parts, sort with merge sort algorithm
- Combine: merge 2 lists by comparing and choose the smaller element

Number of levels = depth = times to divide problems into 1 size: 2^k => t = logn + 1
Operations per level = (number of subproblems) . (work per subproblems)
                    = (2^i) . (cn / 2^i)
Total number of operations = (operations per level) . (number of levels)
                        = (cn) . (logn+1) = cnlogn + cn
O(nlogn)
"""


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


input = list(range(1000))
output = list(range(1000))
random.shuffle(input)

print(mergeSort(input))
