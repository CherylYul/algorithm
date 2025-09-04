"""
Given a string of s, return the minimum number of deletions required
to make it a palindrome. The position of letters does not matter.
Techniques: counting if only char lowercase else hash map
Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter


# counting
def solution(s):
    if len(s) <= 1:
        return 0
    counter = [0] * 26
    for char in s:
        counter[ord(char) - 97] += 1
    deletions = 0
    for num in counter:
        if num and num % 2 == 1:
            deletions += 1
    return deletions - 1 if deletions else deletions


# hash map
def solution2(s):
    if len(s) <= 1:
        return 0
    hash_map = Counter(s)
    deletions = 0
    for key in hash_map:
        if hash_map[key] % 2 == 1:
            deletions += 1
    return deletions - 1 if deletions else deletions


test_cases = [
    {"input": "google", "expected": 1},
    {"input": "aabbcde", "expected": 2},
    {"input": "civic", "expected": 0},
    {"input": "abcdef", "expected": 5},
    {"input": "", "expected": 0},
    {"input": "aabbccdd", "expected": 0},
]


for test in test_cases:
    result = solution(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

for test in test_cases:
    result = solution2(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/min-deletions-to-form-palindrome.py
