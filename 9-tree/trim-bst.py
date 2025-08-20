"""
Leet code 669: Trim a Binary Search Tree
Techniques: Recursion, DFS
Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree due to recursion stack
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimBST(self, root, low, high):
        if not root:
            return root
        if low <= root.val <= high:
            if root.left:
                root.left = self.trimBST(root.left, low, high)
            if root.right:
                root.right = self.trimBST(root.right, low, high)
            return root
        root = root.right if root.val < low else root.left
        return self.trimBST(root, low, high) if root else root
