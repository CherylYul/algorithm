"""
Given a positive integer n, find a pair of positive integers [a, b]
such that a + b = n, neither a nor b can contain digit 0.
Constraints: 2 <= n <= 500,000
Techniques: normal traversal
Complexity: O(nlog(len(n)))
Space Complexity: O(1)
"""


def has_zero(num):
    return "0" in str(num)


def solution(n):
    for a in range(1, n):
        b = n - a
        if not has_zero(a) and not has_zero(b):
            return [a, b]
    return None


test_cases = [
    {"input": 2, "expected": [1, 1]},
    {"input": 10, "expected": [1, 9]},
    {"input": 11, "expected": [2, 9]},
    {"input": 20, "expected": [1, 19]},
    {"input": 30, "expected": [1, 29]},
    {"input": 100, "expected": [1, 99]},
    {"input": 101, "expected": [2, 99]},
    {"input": 400000, "expected": [1, 399999]},
]

for test in test_cases:
    input_value = test["input"]
    expected_output = test["expected"]
    assert solution(input_value) == expected_output

# python3 codility/zero-free-sum.py
