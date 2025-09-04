"""
Given two arrays x and y of the same length n, check if
all points (x[i], y[i]) lie on the perimeter of a square.
Techniques: min, max
Complexity: O(n)
Space Complexity: O(1)
"""


def check_points(x, y, start, end):
    print("check: ", start, end)
    for i in range(len(x)):
        if x[i] != start[0] and x[i] != end[0] and y[i] != start[1] and y[i] != end[1]:
            return False
    return True


def solution(x, y):
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    if max_x - min_x > max_y - min_y:
        if max_y == min_y:
            print("it's an Ox line!")
            return True
        print("case a: keep width, extend height")
        diff = max_x - min_x
        if check_points(x, y, [min_x, min_y], [max_x, min_y + diff]):
            return True
        if check_points(x, y, [min_x, max_y - diff], [max_x, max_y]):
            return True
        return False
    if max_y - min_y > max_x - min_x:
        if max_x == min_x:
            print("It's an Oy line!")
            return True
        print("case b: keep height, extend width")
        diff = max_y - min_y
        if check_points(x, y, [min_x, min_y], [min_x + diff, max_y]):
            return True
        if check_points(x, y, [max_x - diff, min_y], [max_x, max_y]):
            return True
        return False
    print("case c")
    return check_points(x, y, [min_x, min_y], [max_x, max_y])


test_cases = [
    {"input": ([0, 0, 0, 0], [1, 2, 3, 4]), "expected": True},
    {"input": ([0, 0, 0, 0, 3], [0, 2, 5, 7, 0]), "expected": True},
    {"input": ([-1, 1, -2], [2, 1, 0]), "expected": True},
    {"input": ([-1, 2, -2], [2, 1, 0]), "expected": True},
    {"input": ([-1, 2, -2, 1], [2, 1, 0, 0]), "expected": False},
    {"input": ([-1, 1, -1, -2], [2, 1, 1, 0]), "expected": False},
    {"input": ([-10, -10, -10, -9], [-10, 10, 10, 5]), "expected": True},
    {"input": ([-1, 1, 1, -1, 0], [1, 1, -1, -1, 0]), "expected": False},
    {"input": ([0, 1, 2], [0, 1, 2]), "expected": False},
    {"input": ([4, 6, 7, 10], [8, 2, 8, 5]), "expected": True},
    {"input": ([4, 5, 6, 7, 10], [8, 4, 2, 8, 5]), "expected": False},
]

for i, test_case in enumerate(test_cases):
    result = solution(*test_case["input"])
    print(result)
    assert result == test_case["expected"], f"Test case {i} failed: {result}"

# python3 codility/points-on-square-perimeter.py
