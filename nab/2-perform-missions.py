# In order to finish a game, a player has to complete N missions.
# The missions are numbered from 0 to N - 1
# The K-th mission has an integer D[K] assigned, representing its difficulty level.
# The player can perform any number of missions given the 2 following rules:
# - missions should be performed in the specified order
# - the difference between the difficulty levels of any two consecutive missions should not greater than X
# Given array D contains N integers, and integers X
# returns the minimum number of days required to complete all the missions
# [5, 8, 2, 7] 3 => 3
# [2, 5, 9, 2, 1, 4] 4 => 3
# [1, 12, 10, 4, 5, 2] 2 => 4


def solution(D, X):
    n = len(D)
    count_days = 1
    if D[0] > D[1]:
        min_diff, max_diff = D[1], D[0]
    else:
        min_diff, max_diff = D[0], D[1]
    for i in range(1, n - 1):
        if abs(D[i] - min_diff) <= X and abs(D[i] - max_diff) <= X:
            min_diff = min(D[i], min_diff)
            max_diff = max(D[i], max_diff)
        else:
            count_days += 1
            if D[i] < D[i + 1]:
                min_diff, max_diff = D[i], D[i + 1]
            else:
                max_diff, min_diff = D[i], D[i + 1]
    if abs(D[n - 1] - min_diff) > X or abs(D[n - 1] - max_diff) > X:
        count_days += 1

    return count_days


print(solution([5, 8, 2, 7], 3))  # 3
print(solution([2, 5, 9, 2, 1, 4], 4))  # 3
print(solution([1, 12, 10, 4, 5, 2], 2))  # 4

# python3 nab/perform-missions.py
