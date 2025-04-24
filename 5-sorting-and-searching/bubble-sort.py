tests = []
# Case 1: input already sorted
tests.append(
    {
        "input": [24, 35, 55, 67, 77, 87, 90, 91],
        "output": [24, 35, 55, 67, 77, 87, 90, 91],
    }
)
# Case 2: input is randomly
tests.append(
    {
        "input": [69, 35, 55, 40, 41, 42, 63, 71],
        "output": [35, 40, 41, 42, 55, 63, 69, 71],
    }
)
# Case 3: input is in decreasing order also repeating list
tests.append(
    {
        "input": [99, 98, 94, 94, 94, 92, 91, 90, 89, 88, 88, 87],
        "output": [87, 88, 88, 89, 90, 91, 92, 94, 94, 94, 98, 99],
    }
)

"""
Identify adjacent pairs of elements that are out of order, and perform repeated 
swaps until the entire array is sorted

- smaller elements bubble to the top, larger sink to the bottom
- iterate elements in the list, compare if the left element larger than the next one, swap it, 
repeat it n-1 times, each time the times to compare decrease

The worst case happens when our list in the descending order O(n^2)
"""


def bubbleSort(a):
    a = list(a)
    for pos in range(len(a)):
        for i in range(1, len((a)) - pos):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
    return a
