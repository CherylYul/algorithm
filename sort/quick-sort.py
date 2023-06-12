import random

tests = []
# Case 1: the rating already sorted
tests.append(
    {
        "input": [2.4, 3.5, 5.5, 6.7, 7.7, 8.7, 9.0, 9.1],
        "output": [2.4, 3.5, 5.5, 6.7, 7.7, 8.7, 9.0, 9.1],
    }
)
# Case 2: the rating is randomly
tests.append(
    {
        "input": [6.9, 3.5, 5.5, 4.0, 4.1, 4.2, 6.3, 7.1],
        "output": [3.5, 4.0, 4.1, 4.2, 5.5, 6.3, 6.9, 7.1],
    }
)
# Case 3: the rating is in decreasing order also repeating list
tests.append(
    {
        "input": [9.9, 9.8, 9.4, 9.4, 9.4, 9.2, 9.1, 9.0, 8.9, 8.8, 8.8, 8.7],
        "output": [8.7, 8.8, 8.8, 8.9, 9.0, 9.1, 9.2, 9.4, 9.4, 9.4, 9.8, 9.9],
    }
)


def quick_sort(a, start=0, end=None):
    if end is None:
        end = len(a) - 1
    if start < end:
        pivot = partition2(a, start, end)
        quick_sort(a, start, pivot - 1)
        quick_sort(a, pivot + 1, end)
    return a


def partition1(a, start=0, end=None):
    if end is None:
        end = len(a) - 1
    l, r = start, end - 1
    while r > l:
        if a[l] <= a[end]:
            l += 1
        elif a[r] > a[end]:
            r -= 1
        else:
            a[r], a[l] = a[l], a[r]
    if a[l] > a[end]:
        a[l], a[end] = a[end], a[l]
        return l
    else:
        return end


def partition2(a, start, end):
    x = a[end]
    i = start - 1
    for j in range(start, end - 1, 1):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[end] = a[end], a[i + 1]
    return i + 1


def randomized_quicksort(a, start, end):
    if start < end:
        pivot = randomized_partition(a, start, end)
        randomized_quicksort(a, start, pivot - 1)
        randomized_quicksort(a, pivot + 1, end)
    return a


def randomized_partition(a, start, end):
    i = random.randint(start, end)
    a[end], a[i] = a[i], a[end]
    return partition2(a, start, end)


print(quick_sort(tests[2]["input"]) == tests[2]["output"])
