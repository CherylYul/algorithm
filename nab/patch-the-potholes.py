# Given X and Y as position of the potholes, W is the width of car
# Calculate the minimum drives will be needed to patch all the potholes
# Ex: X = [2, 4, 2, 6, 7, 1] Y = [0, 5, 3, 2, 1, 5] W = 2 => 3
# Ex: X = [4, 8, 2, 2, 1, 4] Y = [1, 2, 3, 1, 2, 3] W = 3 => 2
# Ex: X = [0, 3, 6, 5] Y = [0, 3, 2, 4] W = 1 => 3


def solution(X, Y, W):
    if len(X) == 0:
        return 0
    potholes_pos = X
    potholes_pos.sort()
    n = len(X)
    current_pos = potholes_pos[0]
    drive_count = 1
    for i in range(1, n):
        if potholes_pos[i] > current_pos + W:
            current_pos = potholes_pos[i]
            drive_count += 1
    return drive_count


test_cases = [
    {
        "X": [2, 4, 2, 6, 7, 1],
        "Y": [0, 5, 3, 2, 1, 5],
        "W": 2,
    },
    {
        "X": [4, 8, 2, 2, 1, 4],
        "Y": [1, 2, 3, 1, 2, 3],
        "W": 3,
    },
    {
        "X": [0, 3, 6, 5],
        "Y": [0, 3, 2, 4],
        "W": 1,
    },
]

for test in test_cases:
    X, Y, W = test["X"], test["Y"], test["W"]
    print(solution(X, Y, W))

# python3 nab/patch-the-potholes.py
