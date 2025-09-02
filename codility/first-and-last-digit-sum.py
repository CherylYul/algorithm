"""
Given an array of a, find the maximum possible of 2 numbers x and y
where first and last digit of x and y are the same. Return max value,
if not return -1
Techniques: hash map
Complexity: O(n)
Space: O(n)
"""


def solution(a):
    hash_map = {}
    for num in a:
        s_num = str(num)
        key = (s_num[0], s_num[-1])
        if key not in hash_map:
            hash_map[key] = [num, -1]
        else:
            largest, second_largest = hash_map[key]
            if num > largest:
                hash_map[key] = [num, largest]
            elif num > second_largest:
                hash_map[key] = [largest, num]
    best = -1
    for key in hash_map:
        if hash_map[key][1] != -1:
            best = max(hash_map[key][0] + hash_map[key][1], best)

    return best if best > -1 else -1


test_cases = [
    {"input": [30, 319, 200, 20, 200, 320, 300, 3290], "expected": 3610},
    {"input": [30, 29, 384, 650], "expected": -1},
    {"input": [30, 319, 400, 400, 310], "expected": 800},
    {"input": [5, 55, 555], "expected": 610},
    {"input": [1, 2, 3, 4, 5], "expected": -1},
    {"input": [10, 20, 30, 40, 50], "expected": -1},
    {"input": [11, 22, 33, 44, 55], "expected": -1},
]

for test in test_cases:
    input_value = test["input"]
    expected_output = test["expected"]
    assert solution(input_value) == expected_output


# python3 codility/first-and-last-digit-sum.py
