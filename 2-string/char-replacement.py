"""
Given a string s and an integer k. You can choose any character and
change it to any other uppercase English character at most k times.
Return the length of the longest substring containing the same letter.
s = "ABAB" k = 2 => "AAAA" => 4
s = "AABABBA" k = 1 => "AAABBA" => 4
Solution: sliding window + pointer
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def characterReplacement(self, s, k):
        hash_table, l, max_count = {}, -1, 0
        for r in range(len(s)):
            hash_table[s[r]] = hash_table.get(s[r], 0) + 1
            max_count = max(max_count, hash_table[s[r]])
            if r - l - max_count > k:
                l += 1
                hash_table[s[l]] -= 1
        return len(s) - l
