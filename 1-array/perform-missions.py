"""
NAB 2023 - Perform Missions
Problem: Given a list of daily mission difficulties and a maximum allowed difference X,
count the minimum number of days required to complete all missions, where each day can only handle missions
within a certain difficulty range defined by X.
Solution: Sliding window approach
Time Complexity: O(n), where n is the number of days.
Space Complexity: O(1), no additional space used.
"""


def solution(D, X):
    if not D:
        return 0
    if len(D) == 1:
        return 1

    max_day, min_day, count = 0, 0, 1
    for i in range(len(D)):
        if not max_day or D[i] > max_day:
            max_day = D[i]
        if not min_day or D[i] < min_day:
            min_day = D[i]
        if max_day - min_day <= X:
            continue
        else:
            count += 1
            max_day, min_day = D[i], D[i]
    return count


print(solution([5, 8, 2, 7], 3))  # 3
print(solution([2, 5, 9, 2, 1, 4], 4))  # 3
print(solution([1, 12, 10, 4, 5, 2], 2))  # 4

# python3 1-array/perform-missions.py
