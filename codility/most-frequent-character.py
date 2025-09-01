"""
Given string s, return the most frequent character in it.
If not, return the first character in alphabetical order.
Constraints: 1 <= |s| <= 100,000
Techniques: Counting
Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter


def solution(s):
    counter = [0] * 26
    for char in s:
        counter[ord(char) - 97] += 1
    best, idx = 0, 0
    for i in range(26):
        if counter[i] > best:
            best, idx = counter[i], i
    return chr(idx + 97)


def shortestSolution(s):
    counts = Counter(s)
    return max(sorted(counts.keys()), key=lambda x: (counts[x], -ord(x)))


test_cases = [
    {"input": "ddcc", "expected": "c"},
    {"input": "zyxw", "expected": "w"},
    {"input": "abcabc", "expected": "a"},
    {"input": "aabbcc", "expected": "a"},
    {"input": "zaab", "expected": "a"},
    {"input": "abc", "expected": "a"},
    {"input": "a", "expected": "a"},
    {"input": "ab", "expected": "a"},
]

for test in test_cases:
    input_value = test["input"]
    expected_output = test["expected"]
    assert solution(input_value) == expected_output
    assert shortestSolution(input_value) == expected_output

# python3 codility/most-frequent-character.py
