"""
LeetCode 235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution(object):
    # iterative
    # Time complexity: O(n)
    # Space complexity: O(1)
    def lowestCommonAncestor1(self, root, p, q):
        if root == p or root == q:
            return root
        if p.val >= q.val:
            large, small = p, q
        else:
            large, small = q, p

        while root:
            if small.val <= root.val <= large.val:
                return root
            root = root.right if root.val < small.val else root.left

    # recursive
    # Time complexity: O(n)
    # Space complexity: O(n)
    def lowestCommonAncestor2(self, root, p, q):
        if not root or root == q or root == p:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left and right:
            return root
        return left or right
