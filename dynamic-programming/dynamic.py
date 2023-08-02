rods = {
    "length": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price": [0, 1, 5, 6, 9, 10, 17, 17, 20, 24, 30],
}


# O(n^2)
def cut_rod(n, value_list):
    if n == 0:
        return 0
    optimize = -float("inf")
    for i in range(1, n + 1):
        optimize = max(optimize, value_list[i] + cut_rod(n - i, value_list))
    return optimize


# O(n^2) ~ DFS
def memoized(n, value_list):
    a = [-float("inf") for _ in range(n + 1)]
    return internal_memoized(n, a, value_list)


def internal_memoized(n, a, value_list):
    if a[n] >= 0:
        return a[n]
    if n == 0:
        return 0
    optimize = -float("inf")
    for i in range(1, n + 1):
        optimize = max(
            optimize, value_list[i] + internal_memoized(n - i, a, value_list)
        )
    a[n] = optimize
    return optimize


# O(n^2) ~ topological sort
def bottom_up(n, value_list):
    a = [-float("inf") for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n + 1):
        optimize = -float("inf")
        for i in range(1, j + 1):
            optimize = max(optimize, value_list[i] + a[j - i])
        a[j] = optimize
    return a[n]


def extend_bottom_up(n, value_list):
    s = [None for _ in range(n + 1)]
    a = [None for _ in range(n + 1)]
    a[0] = 0
    for j in range(1, n + 1):
        optimize = -float("inf")
        for i in range(1, j + 1):
            if optimize < value_list[i] + a[j - i]:
                optimize = value_list[i] + a[j - i]
                s[j] = i
        a[j] = optimize
    return s, a


def print_solution(n, value_list):
    s, a = extend_bottom_up(n, value_list)
    str = ""
    for i in range(n + 1):
        str += "{}: {}, {} \n".format(i, a[i], s[i])
    return str


"""
Matrix-chain multiplication problem: build an optimal solution to an divide matrix-chain
problem into 2 subproblems, then combine the optimal solutions (at least multiplication
as possible)
"""

"""
Longest common subsequence: compare DNA of 2 or more organisms to know how closely related
the 2 organisms are
1. lcs recursive: O(2^(n+m))
2. lcs dynamic programing: O(n*m)
"""
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
s3 = "GTCGTCGGAAGCCGGCCGAA"
s4 = "alchemy"
s5 = "analogy"
s6 = "aly"
s7 = "TAGTCACG"
s8 = "AGACTGTC"


def lcs_recursive(seq1, seq2, idx1, idx2):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    if seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        return max(
            lcs_recursive(seq1, seq2, idx1 + 1, idx2),
            lcs_recursive(seq1, seq2, idx1, idx2 + 1),
        )


def lcs_memoized(seq1, seq2, idx1, idx2, memo={}):
    key = (idx1, idx2)
    if key in memo:
        return memo[key]
    if idx1 == len(seq1) or idx2 == len(seq2):
        memo[key] = 0
    elif seq1[idx1] == seq2[idx2]:
        memo[key] = 1 + lcs_memoized(seq1, seq2, idx1 + 1, idx2 + 1, memo)
    else:
        memo[key] = max(
            lcs_memoized(seq1, seq2, idx1, idx2 + 1, memo),
            lcs_memoized(seq1, seq2, idx1 + 1, idx2, memo),
        )
    return memo[key]


def lcs_dp(seq1, seq2):
    table = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]
    for i in range(seq1):
        for j in range(seq2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
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

# print(cut_rod(4, rods["price"]))
# print(memoized(4, rods["price"]))
# print(bottom_up(4, rods["price"]))
# print(print_solution(10, rods["price"]))
print(lcs_memoized(s1, s2, 0, 0))
# python3 dynamic-programming/dynamic.py
