"""
Leet code 49: Group Anagrams
Techniques: Hash Map, Sorting, Counting
Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n * k) for the hash map
"""


class Solution(object):
    # sorting
    def groupAnagrams(self, strs):
        hash_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return [hash_map[key] for key in hash_map]

    # counting
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]
        hash_map = {}
        for s in strs:
            counter = [0] * 26
            for char in s:
                counter[ord(char) - 97] += 1
            key = ".".join(str(num) for num in counter)
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return [hash_map[key] for key in hash_map]
