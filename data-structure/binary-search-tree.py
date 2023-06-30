import random


class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return "Node {}".format(self.key)

    def __str__(self):
        return self.__repr__()


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    """
    Insert: O(logn)
    1. Find right position of value in the tree: find which node in the tree is
    value's parent
    2. Insert:
    - If tree doesn't have elements, then parent is None, insert value AS A NODE
    to the root of the tree
    - If there is parent, insert value to the left or right by comparing the value
    with parent key, insert value AS A NODE with parent argument

    Ex: insert 13 to                    12
                                5                   18
                            2       9       15              19
                                         ...   17
    """

    def insert(self, value):
        parent = self.find_parent(self.root, None, value)
        if not parent:
            self.root = Node(value)
        else:
            if value <= parent.key:
                parent.left = Node(value, None, None, parent)
            else:
                parent.right = Node(value, None, None, parent)
        self.size += 1

    """
    Find_parent: O(logn): find the right value's parent to support the insert process

    Method 1: use loop
    def find_parent(self, value):
        x, parent = self.root, None
        while x:
            parent = x
            if value <= x.key:
                x = x.left
            else:
                x = x.right
        return parent

    Method 2: use divide and conquer
    - default: node = self.root, parent = None
    - base case: recurse to a node that is None, return parent
    - compare value with node.key to decide recurse to node.left or node.right
    """

    def find_parent(self, node, parent, value):
        if not node:
            return parent
        parent = node.key
        if value <= node.key:
            return self.find_parent(node.left, node, value)
        return self.find_parent(node.right, node, value)

    """
    Search: O(logn)
    Minimum: O(logn)
    Maximum: O(logn)
    """

    def search(self, value):
        return self.internal_search(self.root, value)

    def internal_search(self, node, value):
        if not node:
            return None
        if value == node.key:
            return node
        if value <= node.key:
            return self.internal_search(node.left, value)
        return self.internal_search(node.right, value)

    def minimum(self):
        return self.internal_minimum(self.root)

    def internal_minimum(self, node):
        while node and node.left:
            node = node.left
        return node

    def maximum(self):
        return self.internal_maximum(self.root)

    def internal_maximum(self, node):
        while node and node.right:
            node = node.right
        return node

    """
    Successor: O(logn) there are 2 cases:
    1. If node.right exists, then successor of node.key is the left most of
    node's right subtree, ex: successor(15) = 17, find it by calling minimum in
    the node.right
    2. If node.right is empty, the successor of node.key is finding by going up
    the tree until reach the one which is left node of its parent, then return the
    parent, ex: successor(13) = 15   
                            15
                    6               18
                3       7       17      20
              2   4       13
                        9
    Predecessor: O(logn) are symmetric to successor:
    1. If node.left exists, then predecesscor of node.key is the right most of the
    node's left subtree, ex: predecessor(15) = 13
    2. If node.left is empty, the the predecessor of node.key is finding by going up
    until reach the one which is right node of its parent, then return the parent, ex:
    predecessor(17) = 15
    """

    def successor(self, value):
        node = self.search(value)
        if not node:
            return None
        if node.right:
            return self.internal_minimum(node.right)
        while node.parent and node != node.parent.left:
            node = node.parent
        return node.parent

    def predecessor(self, value):
        node = self.search(value)
        if not node:
            return None
        if node.left:
            return self.internal_maximum(node.left)
        while node.parent and node != node.parent.right:
            node = node.parent
        return node.parent

    """ 
    Delete: O(logn) there are 2 cases:
    1. Delete_node only has 1 leaf on the left or right, simply remove it, replace the
    right leaf or left leaf to current position
    2. Delete_node has 2 leaves, find the successor by calling internal_minimum in 
    node.right, this successor (next_node) can't have left side since it is smallest, 
    it may have right side.
    - If next_node is directly connected to delete_node, remove delete_node, replace the
    next_node. 
    - If next_node is not connected to delete_node, ex delete node 15, replace 16 by 17,
    then replace 15 by 16
    Ex:          _______________12_______________
        ________5________                ________20________
        2____           9         ______15______          22
            3                    13          __18__
                                           16__    19
                                              17
    """

    def delete(self, value):
        node = self.search(value)
        if not node:
            return None
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            next_node = self.internal_minimum(node.right)
            if next_node.parent != node:
                self.transplant(next_node, next_node.right)
                next_node.right = node.right
                next_node.right.parent = next_node
            self.transplant(node, next_node)
            next_node.left = node.left
            next_node.left.parent = next_node
        self.size -= 1

    """
    Transplant: O(1) change the old node to new node
    1. If the remove_node is at root then simply replace all the node
    2. If remove_node on the left subtree, then remove_node.parent.left is replaced
    3. If remove_node on the right subtree, then remove_node.parent.right is replaced
    Finally, changing the new node parent.
    """

    def transplant(self, rm_node, rpl_node):
        if not rm_node.parent:
            self.root = rpl_node
        elif rm_node == rm_node.parent.left:
            rm_node.parent.left = rpl_node
        else:
            rm_node.parent.right = rpl_node
        if rpl_node:
            rpl_node.parent = rm_node.parent

    """
    1. Inorder tree walk: prints value in left, then the root, and finally the right O(n)
    2. Preorder tree walk: prints the root before the values in either subtree
    3. Postorder tree walk: prints the root after the values in its subtrees.
    """

    def traverse_in_order(self, node):
        if not node:
            return None
        self.traverse_in_order(node.left)
        print(node.key)
        self.traverse_in_order(node.right)

    def traverse_pre_order(self, node):
        if not node:
            return None
        print(node.key)
        self.traverse_pre_order(node.left)
        self.traverse_pre_order(node.right)

    def traverse_post_order(self, node):
        if not node:
            return None
        self.traverse_post_order(node.left)
        self.traverse_post_order(node.right)
        print(node.key)

    def display_tree(self, node, space="         ", depth=0):
        if node is None:
            print(space * depth, "x")
            return
        if node.left == None and node.right == None:
            print(space * depth, node.key)
            return
        self.display_tree(node.left, space, depth + 1)
        print(space * depth, node.key)
        self.display_tree(node.right, space, depth + 1)

    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))


def simple_test():
    tests = []
    tests.append([12, 5, 18, 2, 9, 15, 19, 17])
    tests.append([15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9])
    tests.append([12, 5, 20, 2, 9, 15, 22, 3, 13, 18, 16, 19, 17])
    for test in tests:
        bst = BST()
        for v in test:
            bst.insert(v)
        print("1: tree from beginning: ")
        bst.traverse_in_order(bst.root)
        print("2: insert 13: ")
        bst.insert(13)
        bst.traverse_in_order(bst.root)
        print("3: search 20: ")
        print(bst.search(20))
        print("4: minimum and maximum: ")
        print(bst.minimum(), bst.maximum())
        print("5: predecessor 15 and successor 13: ")
        print(bst.predecessor(15), bst.successor(13))
        bst.display_tree(bst.root)
        print("6: delete 15: ")
        bst.delete(15)
        bst.display_tree(bst.root)
        print("7: depth: ")
        print(bst.depth(bst.root))


def random_test():
    bst = BST()
    values = []
    for i in range(100):
        value = random.randint(-30, 30)
        values.append(value)
        bst.insert(value)
    assert list(bst) == sorted(values)

    nums = random.sample(values, 40)
    for num in nums:
        bst.delete(num)
        assert len(bst) == len(values) - 1
        bst.insert(num)
        assert len(bst) == len(values)

    assert list(bst) == sorted(values)


simple_test()
