"""
Given string s of length of length n contains only 'R' and 'W' balls.
Return the minimum number of swaps required to group all 'R's together.
In one move, we can only swap 2 adjacent balls.
Techniques: prefix suffix sum
Time complexity: O(n)
Space complexity: O(1)
"""


def create_prefix(s):
    prefix, num_w = [], 0
    for r in s:
        if r == "R":
            prev_sum = prefix[-1] if prefix else 0
            prefix.append(num_w * len(prefix) + prev_sum)
            num_w = 0
        else:
            num_w += 1
    print(prefix)
    return prefix


def solution(s):
    prefix, suffix = create_prefix(s), create_prefix(s[::-1])
    min_step, n = float("inf"), len(prefix)
    for i in range(n):
        min_step = min(min_step, prefix[i] + suffix[n - 1 - i])
    return min_step if min_step <= pow(10, 9) else -1


test_cases = [
    {"input": "WRRWWR", "expected": 2},
    {"input": "RWRWRWWR", "expected": 5},
    {"input": "RRRRRWWW", "expected": 0},
    {"input": "WWRWRRWR", "expected": 2},
    {"input": "RRWWRR", "expected": 4},
    {"input": "RRWWRRRWWWR", "expected": 7},
]


for test in test_cases:
    result = solution(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/min-swap-to-group-reds.py
