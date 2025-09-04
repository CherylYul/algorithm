"""
Given an array of int, create pairs of them, such that every pair
consists of equal numbers, each array element may belong to one pair
only. Is it possible to use all of the integers in the array?
Constraints: n [1, 100,000] values [1, 1,000,000,000]
Techniques: hash map
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter


def solution(values: list[int]) -> bool:
    hash_map = {}
    for v in values:
        hash_map[v] = hash_map.get(v, 0) + 1
    for v in hash_map:
        if hash_map[v] % 2 == 1:
            return False
    return True


# use Counter
def solution2(values):
    hash_map = Counter(values)
    for count in hash_map.values():
        if count % 2 == 1:
            return False
    return True


test_cases = [
    {"input": [1, 2, 2, 1], "expected": True},
    {"input": [7, 7, 7], "expected": False},
    {"input": [1, 1, 2, 2], "expected": True},
    {"input": [1, 2, 3, 4], "expected": False},
    {"input": [1, 1, 1, 1], "expected": True},
]

for test in test_cases:
    result = solution(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/check-pairs.py
