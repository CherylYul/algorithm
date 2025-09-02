"""
Given an array of values, return true if every numbers
not appearing more than l times and all the elements
are less than or equal to k.
You can only change 3 lines of code.
"""


def debug_problems(values: list[int], l: int, k: int) -> int:
    n = len(values)
    for i in range(l, n):
        if values[i - l] == values[i] - l:
            return False
    return values[n] == k


def solution(values: list[int], l: int, k: int) -> int:
    n = len(values)
    for num in set(values):
        if values.count(num) > l or num > k:
            return False
    return True
