"""
Given a 3-digit integer n and an integer k, returns the maximum
possible 3-digit value that can be obtained by performing at most
k increases by 1 of any digit in n.
Constraints: n [100, 999] k [0, 30]
Techniques: normal traverse
Complexity: O(1)
Space: O(1)
"""


def solution(n, k):
    if k == 0:
        return n
    ans, s = "", str(n)
    # digits = [int(d) for d in str(n)]
    for i in range(3):
        num = int(s[i])
        if num + k <= 9:
            ans = ans + str(num + k) + s[i + 1 :]
            break
        ans += "9"
        k = (num + k) - 9
    # return int("".join(str(d) for d in digits))
    return int(ans)


test_cases = [
    {"input": (512, 10), "expected": 972},
    {"input": (487, 2), "expected": 687},
    {"input": (888, 4), "expected": 999},
    {"input": (999, 5), "expected": 999},
    {"input": (100, 19), "expected": 992},
    {"input": (123, 0), "expected": 123},
]

for test in test_cases:
    input_value = test["input"]
    expected = test["expected"]
    assert solution(*input_value) == expected

# python3 codility/max-three-digits.py
