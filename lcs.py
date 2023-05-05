def lcs(seq1, seq2, idx1=0, idx2=0):
    if len(seq1[idx1:]) == 0 or len(seq2[idx2:]) == 0:
        return 0
    if seq1[idx1] == seq2[idx2]:
        return lcs(seq1, seq2, idx1 + 1, idx2 + 1) + 1
    else:
        option1 = lcs(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


s1 = "serendipituous"
s2 = "precipitation"
print(lcs(s1, s2))


def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 * (n2 + 1)] * (n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    return table[-1][-1]


def knapsack_prob(profit, weight, capacity):
    table = [[0 for x in range(len(weight) + 1)] for x in range(capacity + 1)]
    for c in range(1, capacity + 1):
        for i in range(1, len(weight) + 1):
            current_player_w = weight[i - 1]
            current_player_p = profit[i - 1]
            if c < current_player_w:
                table[c][i] = table[c][i - 1]
            else:
                table[c][i] = max(
                    table[c][i - 1],
                    table[c - current_player_w][i - 1] + current_player_p,
                )
    print(table)
    return table[-1][-1]


profit = [2, 3, 1, 5, 4, 7]
weight = [4, 5, 1, 3, 2, 5]
capacity = 15

print(knapsack_prob(profit, weight, capacity))
