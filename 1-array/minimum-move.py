"""
Minimum Moves to Make Array Elements Equal
There is an array A of N integers sorted in non-decreasing order.
In 1 move, you can either remove an integer from A or insert an integer before or after any element of A.
The goal is to achieve an array in which all values X that are present in the array occur exactly X times.
Solution: counting elements subjects
Time complexity: O(N)
Space complexity: O(N)
"""


def solution(A):
    counters = {}
    steps = 0
    for num in A:
        counters[num] = counters.get(num, 0) + 1
    for key in counters:
        if counters[key] == key:
            print(key, "Don't need to change: ", steps)
            continue
        if counters[key] > key:
            steps += counters[key] - key
            print(key, "Too many numbers, remove: ", steps)
        else:
            mid = key // 2
            if counters[key] > mid:
                steps += key - counters[key]
                print(key, "Larger than mid, add: ", steps)
            else:
                steps += counters[key]
                print(key, "Smaller than mid, remove: ", steps)
    return steps


test_cases = [
    {"A": [1, 1, 3, 4, 4, 4], "expected": 3},
    {"A": [1, 2, 2, 2, 5, 5, 5, 8], "expected": 4},
]

for test in test_cases:
    A, expected = test["A"], test["expected"]
    print(solution(A) == expected)

# python3 1-array/minimum-move.py
