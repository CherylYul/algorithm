"""
Leet Code 104: Maximum Depth of Binary Tree
Techniques: recursion and breadth-first search (BFS)
Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree due to recursion stack or
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # recursion
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # BFS
    def maxDepth(self, root):
        if not root:
            return 0
        q = deque()
        q.append(root)
        height = 0
        while q:
            height += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return height
