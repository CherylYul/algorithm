"""
There are N players standing in a row, one player on a field.
They are numbered from 0 to N - 1 from left to right.
Players perform moves one by one from left to right, that is, in ascending order of numbers.
Each player presses an arrow key in 1 of the 4 cardinal directions: left('<'), right('>'), up('^'), or down('v').
A key press in the given direction means that the player attempts to move onto the closest field in the direction specified
A move can be performed only if there is no other player already standing on the target field
"""


def performMoves(str):
    empty, count = True, 0
    for move in str:
        if move == "^" or move == "v":
            count += 1
            empty = True
        if move == "<" and empty:
            count += 1
        if move == ">":
            empty = False
    if str[-1] == ">":
        count += 1
    return count


test_cases = [
    {"input": "><^^", "expected": 2},
    {"input": "><><", "expected": 0},
    {"input": "><^v", "expected": 2},
    {"input": "><^<", "expected": 2},
    {"input": "><^>v", "expected": 2},
    {"input": "><^>v<", "expected": 3},
]

for test in test_cases:
    input, expected = test["input"], test["expected"]
    print(performMoves(input) == expected)

# python3 2-string/move-players.py
