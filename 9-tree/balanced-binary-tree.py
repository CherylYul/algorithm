"""
Solution: Depth-First Search (DFS) to check balance and height of the tree.
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree due to recursion stack.
"""


class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root:
                return [True, 0]
            l_balance, l_height = dfs(root.left)
            r_balance, r_height = dfs(root.right)
            return [
                l_balance and r_balance and abs(l_height - r_height) <= 1,
                1 + max(l_height, r_height),
            ]

        return dfs(root)[0]
