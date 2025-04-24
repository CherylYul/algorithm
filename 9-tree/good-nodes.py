class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # recursion: Time O(n), Space O(h)
    def goodNodes(self, root):
        def dfs(self, root, maxValue):
            if not root:
                return 0
            if root.val >= maxValue:
                return (
                    1 + dfs(self, root.left, root.val) + dfs(self, root.right, root.val)
                )
            return dfs(self, root.left, maxValue) + dfs(self, root.right, maxValue)

        return dfs(self, root, root.val)

    # stack: Time O(n), Space O(n), only use when we check each node, and forget it right after
    def goodNodes2(self, root):
        if not root:
            return 0

        num_of_goodnodes = 0
        stack = [(root, -float("inf"))]
        while stack:
            node, max_val = stack.pop(0)
            if node.val >= max_val:
                num_of_goodnodes += 1
                max_val = node.val
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))

        return num_of_goodnodes
