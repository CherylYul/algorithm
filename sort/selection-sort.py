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
Selection sort scans through the input array to identify the minimum element and
swap with element at current position
Step 1: iterate the variables in the list
Step 2: with each, compare the current with values after, find the lowest number
Step 3: Swap the lowest value found with current value

O(n^2)
"""


def selectionSort(a):
    for i in range(len(a) - 1):
        lowest_num = i
        for j in range(i + 1, len(a)):
            if a[lowest_num] > a[j]:
                lowest_num = j
        a[i], a[lowest_num] = a[lowest_num], a[i]
    return a
