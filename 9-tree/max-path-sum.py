"""
Leetcode 124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.
Time complexity: O(n) where n is the number of nodes in the tree.
Space complexity: O(h) where h is the height of the tree.
Techniques: DFS, Recursion
"""


class Solution(object):
    def maxPathSum(self, root):
        best = [root.val]

        # keep root, only choose one path value
        def dfs(root):
            if root is None:
                return 0
            r_curr_best = dfs(root.right)
            l_curr_best = dfs(root.left)
            r_curr_best = max(r_curr_best, 0)
            l_curr_best = max(0, l_curr_best)
            # update value by eliminating all previous value
            best[0] = max(root.val + r_curr_best + l_curr_best, best[0])
            return root.val + max(r_curr_best, l_curr_best)

        dfs(root)
        return best[0]
