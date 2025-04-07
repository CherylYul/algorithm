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


print(lcs_memoized(s1, s2, 0, 0))
