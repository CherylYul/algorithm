"""
Leet code 205: Isomorphic Strings
Techniques: Hash Map, Set
Complexity: O(n) where n is the length of the strings
Space Complexity: O(n) for the hash map and set used to track mappings
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        hash_map, mapped = {}, set()
        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] != t[i]:
                return False
            elif s[i] not in hash_map:
                if t[i] in mapped:
                    return False
                mapped.add(t[i])
                hash_map[s[i]] = t[i]
        return True
