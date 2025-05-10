"""
LeetCode 100. Same Tree
Given two binary trees, write a function to check if they are the same or not.
Time complexity: O(min(m, n)) where m and n are the number of nodes in the two trees.
Space complexity: O(h) where h is the height of the tree.
"""


class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
