# O(N) or O(N * log(N))
def solution(A):
    max_value = max(A)
    if max_value <= 0:
        return 1
    counter = [False] * max_value
    for value in A:
        if value <= 0 or counter[value - 1]:
            continue
        counter[value - 1] = True
    for i in range(max_value):
        if not counter[i]:
            return i + 1
    return max_value + 1
