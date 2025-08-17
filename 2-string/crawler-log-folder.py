"""
Leet code 1598: Crawler Log Folder
Techniques: stack, greedy
Complexity: O(n) where n is the number of logs
Space Complexity: O(1) for the counter
"""


class Solution(object):
    def minOperations(self, logs):
        count = 0
        for log in logs:
            if log == "../":
                count -= 1 if count > 0 else 0
            elif log != "./":
                count += 1
        return count
