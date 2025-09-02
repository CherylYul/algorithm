"""
Microsoft Online Assessment - Fair Indexes
Techniques: prefix suffix
Complexity: O(n)
Space Complexity: O(1)
"""


def fair_indexes(a: list[int], b: list[int]) -> int:
    same_idx, prefix_a, prefix_b = {}, 0, 0
    for i in range(len(a)):
        prefix_a += a[i]
        prefix_b += b[i]
        if prefix_a == prefix_b:
            same_idx[i] = prefix_a

    suffix_a, suffix_b, count = 0, 0, 0
    for i in range(len(a) - 1, 0, -1):
        suffix_a += a[i]
        suffix_b += b[i]
        if i - 1 in same_idx and suffix_a == suffix_b == same_idx[i - 1]:
            count += 1

    return count


def fair_indexes_optimize_space(a: list[int], b: list[int]) -> int:
    for i in range(1, len(a)):
        a[i] += a[i - 1]
        b[i] += b[i - 1]

    fair = 0
    for k in range(len(a) - 1):
        prefix_a, suffix_a = a[k], a[-1] - a[k]
        prefix_b, suffix_b = b[k], b[-1] - b[k]
        fair += int(prefix_a == suffix_a == prefix_b == suffix_b)
    return fair


test_cases = [
    {"input": ([4, -1, 0, 3], [-2, 5, 0, 3]), "expected": 2},
    {"input": ([2, -2, -3, 3], [0, 0, 4, -4]), "expected": 1},
    {"input": ([4, -1, 0, 3], [-2, 6, 0, 4]), "expected": 0},
    {"input": ([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]), "expected": 2},
    {"input": ([3, 2, 6], [4, 1, 6]), "expected": 0},
    {"input": ([2, -2, -3, 3], [0, 0, 4, -4]), "expected": 1},
]

for test in test_cases:
    input_value = test["input"]
    expected = test["expected"]
    assert fair_indexes(*input_value) == expected

# python3 codility/fair-indexes.py
