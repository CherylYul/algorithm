"""
Leet code 3: Longest Substring Without Repeating Characters
Techniques: sliding window, hash map
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
