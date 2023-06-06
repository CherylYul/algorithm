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


def bubbleSort(a):
    a = list(a)
    for pos in range(len(a)):
        for i in range(1, len((a)) - pos):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
    return a


def selectionSort(a):
    # Iterate the variables in the list
    for i in range(len(a) - 1):
        # With each pass-through, compare the current position with after value in the list, find the lowest number
        lowest_num = i
        for j in range(i + 1, len(a)):
            if a[lowest_num] > a[j]:
                lowest_num = j
        # Swap the value
        a[i], a[lowest_num] = a[lowest_num], a[i]
    return a


def insertionSort(a):
    for i in range(1, len(a)):
        # Create the temp to store the removing value of the index
        current = a[i]
        # Keep compare the stored value with the previous number, if the previous is larger
        # we move to the next position and continue compare the previous one until reach the first element
        # If the previous one is smaller we stop immediately
        j = i - 1
        while j >= 0 and a[j] > current:
            a[j + 1] = a[j]
            j -= 1
        # Adding the stored value to its right position
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


input = list(range(1000))
output = list(range(1000))
random.shuffle(input)

A = [6, 5, 3, 1, 2]
print(bubbleSort(A))
for i, v in enumerate(tests):
    print(bubbleSort(v["input"]) == v["output"])

A = [5, 3, 4, 1, 6]
print(selectionSort(A))
for i, v in enumerate(tests):
    print(selectionSort(v["input"]) == v["output"])

print(insertionSort(A))
for i, v in enumerate(tests):
    print(insertionSort(v["input"]) == v["output"])

A = [5, 4, 1, 8, 7, 2, 6, 3]
print(mergeSort(A))
