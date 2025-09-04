"""
Give a binary string s, convert to decimal number v, then
conduct operations until v = 0, the operations are:
- If v is even, divides v by 2
- If v is odd, subtract by 1
Techniques: Bit Manipulation
Time Complexity: O(n)
Space Complexity: O(1)
"""


def solution(s):
    # idx, num = 0, 0
    # for i in range(len(s) - 1, -1, -1):
    #     num += pow(2, idx) if s[i] == "1" else 0
    #     idx += 1
    num = int(s, 2)
    op = 0
    while num > 0:
        op += 1
        num = num / 2 if num % 2 == 0 else num - 1
    return op


test_cases = [
    {"input": "111", "expected": 5},
    {"input": "100", "expected": 3},
    {"input": "0", "expected": 0},
    {"input": "1111111", "expected": 13},
]

for test in test_cases:
    result = solution(test["input"])
    print(f"Input: {test['input']}, Expected: {test['expected']}, Got: {result}")

# python3 codility/binary-to-zero-operations.py
