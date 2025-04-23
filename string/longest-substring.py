"""
Find the length of the longest substring without duplicate characters
s = "abcabcbb" => "abc" => 3
s = "bbbbb" => "b" => 1
s = "pwwkew" => "wke" => 3
Solution: sliding window + pointer
Time complexity: O(n)
Space complexity: O(1)
"""

"""
You are given a string s and an integer k. You can choose any character of 
the string and change it to any other uppercase English character. You can 
perform this operation at most k times.
Return the length of the longest substring containing the same letter you 
can get after performing the above operations.
s = "ABAB" k = 2 => "AAAA" => 4
s = "AABABBA" k = 1 => "AAABBA" => 4
s = "AABABBA" k = 2 => "AAAAAA" => 6
Solution: sliding window + pointer
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest, l, curr = 0, -1, 0
        hash_s = {}
        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1
            curr += 1
            if hash_s[char] == 1:
                if curr > longest:
                    longest = curr
            else:
                while hash_s[char] > 1:
                    l += 1
                    hash_s[s[l]] -= 1
                    curr -= 1
        return longest

    def characterReplacement(self, s, k):
        hash_table, l, max_count = {}, -1, 0
        for r in range(len(s)):
            hash_table[s[r]] = hash_table.get(s[r], 0) + 1
            max_count = max(max_count, hash_table[s[r]])
            if r - l - max_count > k:
                l += 1
                hash_table[s[l]] -= 1
        return len(s) - l
