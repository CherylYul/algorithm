# O(N + M)
# performance: 60%
def solution(N, A):
    counter = [0] * N
    max = 0
    for i in range(len(A)):
        if A[i] <= N:
            counter[A[i] - 1] += 1
            if counter[A[i] - 1] > max:
                max = counter[A[i] - 1]
        else:
            counter = [max] * N
    return counter


# performance: 100%
def solution(N, A):
    counter = [0] * N
    max_counter = 0
    last_max = 0
    for value in A:
        if value <= N:
            if counter[value - 1] >= last_max:
                counter[value - 1] += 1
            else:
                counter[value - 1] = last_max + 1
            max_counter = max(max_counter, counter[value - 1])
        elif value == N + 1:
            last_max = max_counter
    for i in range(N):
        if counter[i] < last_max:
            counter[i] = last_max
    return counter
