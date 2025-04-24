"""
NAB
Given a string S of length N, returns the length of the shortest unique
substring of S which occurs in S exactly once
Ex: "abaaba" => 2, "aa"
Ex: "zyzyzyz" => 5, "yzyzy"
Ex: "aabbbabaaa"=> 3 , "bba"
"""


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
