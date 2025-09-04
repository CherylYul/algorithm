"""
Given an array of a, return the sum of max even and odd elements.
Constraints: 1 <= a.length <= 1000, -10^6 <= a[i] <= 10^6
Techniques: linear scan, keep track of max even and odd.
Time complexity: O(n)
Space complexity: O(1)
"""


def solution(a):
    odd = even = -float("inf")
    for num in a:
        if num % 2 == 0:
            even = max(even, num)
        else:
            odd = max(odd, num)
    if odd == -float("inf"):
        odd = 0
    if even == -float("inf"):
        even = 0
    return odd + even


test_cases = [
    {"input": [5, 3, 10, 6, 11], "expected": 21},
    {"input": [7, 13, 15, 13], "expected": 15},
    {"input": [2, 6, 4, 6], "expected": 6},
    {"input": [-1, -3, -5, -7], "expected": -1},
    {"input": [-2, -4, -6, -8], "expected": -2},
    {"input": [-1, -4, 6, -8], "expected": 5},
    {"input": [1], "expected": 1},
    {"input": [2], "expected": 2},
    {"input": [0], "expected": 0},
]

for case in test_cases:
    output = solution(case["input"])
    assert (
        output == case["expected"]
    ), f"Test failed for input {case['input']}: expected {case['expected']}, got {output}"

# python3 codility/max-even-odd-sum.py
