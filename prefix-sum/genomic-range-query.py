def solution(S, P, Q):
    n = len(S)
    factor = {"A": 1, "C": 2, "G": 3, "T": 4}
    table = [[0] * (n + 1) for _ in range(4)]
    for i in range(n):
        idx = factor[S[i]] - 1
        table[idx][i + 1] = table[idx][i] + 1

    result = []
    print(table)
    for p, q in zip(P, Q):
        for i in range(4):
            if table[i][q + 1] - table[i][p] > 0:
                result.append(factor[i])
                print(result)
                break
    return result
