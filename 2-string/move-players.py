"""
There are N players standing in a row, one player on a field.
They are numbered from 0 to N - 1 from left to right.
Players perform moves one by one from left to right, that is, in ascending order of numbers.
Each player presses an arrow key in 1 of the 4 cardinal directions: left('<'), right('>'), up('^'), or down('v').
A key press in the given direction means that the player attempts to move onto the closest field in the direction specified
A move can be performed only if there is no other player already standing on the target field
"""


def solution(A):
    for i in A:
        if i in "ud":
            continue


test_cases = [
    {"A": "lrud", "expected": 2},
]

for test in test_cases:
    A, expected = test["A"], test["expected"]
    print(solution(A) == expected)

# python3 1-array/minimum-move.py
