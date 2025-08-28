"""
When increase i by 1, i+1 will also increase by 1,
count the number of steps to make 2 string equal,
if cannot make equal, return -1.
Constraints: 1 <= s.length, t.length <= 10^5
Techniques: normal traversal
Complexity: O(n) where n is the length of the strings
Space Complexity: O(1)
"""


def solution(s, t):
    if s == t:
        return 0
    if len(s) == len(t) == 1:
        return int(t) - int(s) if int(t) >= int(s) else 10 - (int(s) - int(t))
    temp = int(s[-1])
    count = 0
    for i in range(len(s) - 2, -1, -1):
        steps = 0
        if int(t[i + 1]) > temp:
            steps = int(t[i + 1]) - temp
        elif int(t[i + 1]) < temp:
            steps = 10 - (temp - int(t[i + 1]))
        count += steps
        temp = (int(s[i]) + steps) % 10
    return count if temp == int(t[0]) else -1


test_cases = [
    {"s": "13471", "t": "59604", "expected": 9},
    {"s": "557", "t": "403", "expected": 15},
    {"s": "8", "t": "7", "expected": 9},
    {"s": "7115", "t": "6204", "expected": -1},
]

for test in test_cases:
    s, t, expected = test["s"], test["t"], test["expected"]
    print(solution(s, t) == expected)

# python3 codility/count-steps-to-make-equal.py
