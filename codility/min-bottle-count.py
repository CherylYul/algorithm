"""
Given n of bottles from 1 to n, i bottle contains i litter,
what is the minimum bottles we need to contains k litter,
if not possible return -1.
Techniques: normal traverse
Complexity: O(n)
Space Complexity: O(1)
"""


def solution(n, k):
    if k == 0:
        return 0
    for i in range(n, 0, -1):
        k -= i
        if k <= 0:
            return n - i + 1
    return -1


test_cases = [
    {"input": (8, 37), "expected": -1},
    {"input": (8, 36), "expected": 8},
    {"input": (8, 34), "expected": 7},
    {"input": (8, 20), "expected": 3},
    {"input": (3, 3), "expected": 1},
    {"input": (5, 4), "expected": 1},
    {"input": (5, 0), "expected": 0},
]

for test in test_cases:
    result = solution(*test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/min-bottle-count.py
