"""
Given string of s with length n, only include "a" and "b".
Return the number of substrings of length 3 that can be formed
(consecutive characters in the original string).
Constraints: 1 <= n <= 100
Techniques: Sliding Window
Complexity: O(n)
Space: O(1)
"""


def solution(s):
    hash_set = set()
    for i in range(len(s) - 2):
        hash_set.add(s[i : i + 3])
    return len(hash_set)


test_cases = [
    {"input": "", "expected": 0},
    {"input": "a", "expected": 0},
    {"input": "ab", "expected": 0},
    {"input": "aaa", "expected": 1},
    {"input": "aababa", "expected": 3},
    {"input": "ababab", "expected": 2},
    {"input": "bbbbbb", "expected": 1},
]

for test in test_cases:
    result = solution(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/count-3-char-substring.py
