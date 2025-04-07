# NAB Interview
# Write a function solution that, given a string S of length N,
# returns the length of the shortest unique substring of S,
# that is, the length of the shortest word which occurs in S exactly once
# Given a string S = "abaaba", the function should return 2, "aa"
# Given a string S = "zyzyzyz", the function should return 5, "yzyzy"
# Given a string S = "aabbbabaaa", the function should return 3. All substrings of size 2 occurs in S at least twice.


def shortest_unique_substr(s):
    substring_table = {}
    n = len(s)
    for length in range(0, n):
        for i in range(n - length + 1):
            substring = s[i : i + length]
            substring_table[substring] = substring_table.get(substring, 0) + 1
    result = float("inf")
    for str in substring_table:
        if substring_table[str] == 1 and len(str) < result:
            result = len(str)
    if result == float("inf"):
        return -1
    return result


print(shortest_unique_substr("abaaba"))  # 2
print(shortest_unique_substr("zyzyzyz"))  # 5
print(shortest_unique_substr("aabbbabaaa"))  # 3
