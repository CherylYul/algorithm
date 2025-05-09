"""
LeetCode 226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
Time complexity: O(n)
Space complexity: O(n)
Techniques: Recursion
"""


class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
