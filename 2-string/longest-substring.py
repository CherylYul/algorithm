"""
Leet code 3: Longest Substring Without Repeating Characters
Techniques: sliding window, hash map
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, best, hash_map = 0, 0, {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            while hash_map[s[i]] > 1:
                hash_map[s[l]] -= 1
                l += 1
                continue
            best = max(best, i - l + 1)
        return best

    def lengthOfLongestSubstring(self, s):
        l, best, hash_set = 0, 0, set()
        for i in range(len(s)):
            while s[i] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[i])
            best = max(best, i - l + 1)
        return best

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
