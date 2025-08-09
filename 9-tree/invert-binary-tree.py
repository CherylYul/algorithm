"""
Leet Code 226. Invert Binary Tree
Techniques: Recursion and Iteration (BFS)
Time complexity: O(n)
Space complexity: O(n)
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Recursion
    def invertTree(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

    # Iteration (BFS)
    def invertTree(self, root):
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
