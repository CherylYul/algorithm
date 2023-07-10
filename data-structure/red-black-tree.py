"""
A red-black tree is a binary search tree, the node is colored red or black
that satisfies the following red-black properties:
1. Everynode is either red or black
2. The root is black
3. Every leaf NIL is black
4. If a node is red, both its children are black
5. For each node, all simple paths from the node to descendant leaves contain
the same number of black node
Red-black tree ensures the tree is approximately balanced (no such path is more
than twice as long as any other)

A red-black tree with n internal nodes has height at most 2lg(n + 1)
python3 data-structure/red-black-tree.py
"""


class Node:
    def __init__(self, key, left=None, right=None, parent=None, color="B"):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

    def __repr__(self):
        return "Node {}".format(self.key)

    def __str__(self):
        return self.__repr__()


class RBT:
    def __init__(self):
        self.root = None
        self.size = 0

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
    1. Seperate the node x and y, move b from node y to node x
    2. Assemble node y to parent
    3. Assemble node x to y
    Left rotate: O(1)
        x                       y
    a       y       ->      x       c
          b   c           a   b
    
    Right rotate: O(1)
            x                   y
        y       c   ->      a       x
      a   b                       b   c
    """

    def left_rotate(self, x):
        # Seperate the node x and y, move b from node y to node x
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        # Assemble node y to parent
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        # Assemble node x to y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # Seperate the node x and y, move b from node y to node x
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        # Assemble node y to parent
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        # Assemble node x to y
        y.right = x
        x.parent = y

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
    
    In insert_fixup, while loop repeats only if case 1 occurs, and then the pointer
    z moves 2 levels up the tree. The total number of time while loop can be executed
    is O(logn). Moreover, it never performs more than 2 rotations, since while loop
    terminates if case 2 or case 3 is executed
    """

    def insert(self, value):
        parent = self.find_parent(value, self.root, None)
        if not parent:
            self.root = Node(value)
        elif value <= parent.key:
            parent.left = Node(value, None, None, parent, "R")
            self.insert_fixup(parent.left)
        else:
            parent.right = Node(value, None, None, parent, "R")
            self.insert_fixup(parent.right)
        self.size += 1
    
    def insert_fixup(self, node):
        while node.parent.color == "R":
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == "R":
                    y.color = "B"
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.right_rotate(node.parent.parent)
            elif node.parent == node.parent.parent.right:
                y = node.parent.parent.left
                if y.color == "R":
                    y.color = "B"
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "B"
                    node.parent.parent.color = "R"
                    self.left_rotate(node.parent.parent)
        self.root.color = "B"

    """
    Find_parent: O(logn): find the right value's parent to support the insert process

    Method 1: using while loop
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

    def find_parent(self, value, node, parent):
        if not node:
            return parent
        if value <= node.key:
            return self.find_parent(value, node.left, node)
        return self.find_parent(value, node.right, node)
    
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
    What's more?
    1. Keep track of the moving node's color: if delete node falls into case 1 above, 
    we save the node color, if it falls into case 2, we save next node color
    2. When color is red: 
    - No black-heights in the tree have changed
    - No red nodes have been made adjacent. 
    - If it was red, it cannot be a root, root remains black
    3. When color is black:
    - If the color node was at root, some node go to replace may violate property 2
    - If the node to replace is red, the parent of it maybe red before (since the node
    is black) causing property 4 violation
    Ex: delete 2 which is black, replace 3, 3 and 5 maybe red, and there is 2 red 
    adjacent nodes
    - Moving the black node may cause unbalanced, thus violate property 5
    """

    def delete(self, value):
        node = self.search(value)
        next_node_color = node.color  # save node color
        if not node:
            return None
        if not node.left:
            x = node.right
            self.transplant(node, node.right)
        elif not node.right:
            x = node.left
            self.transplant(node, node.left)
        else:
            next_node = self.internal_minimum(node.right)
            next_node_color = next_node.color # save next node color
            x = next_node.right
            if next_node.parent == node:
                x.parent = next_node
            else:
                self.transplant(next_node, next_node.right)
                next_node.right = node.right
                next_node.right.parent = next_node
            self.transplant(node, next_node)
            next_node.left = node.left
            next_node.left.parent = next_node
            next_node.color = node.color
        if next_node_color == "B":
            self.delete_fixup(x)
        self.size -= 1
    
    """
    Checking the node in the while loop in case it is not the root and its color
    is black, we maintain a pointer to its sibling w:

    Case 1: arise when its sibling w is red, since w must have black children, we
    switch the color of w and its parent then perform a left rotation, which turns 
    into case 2, 3, 4
    Case 2: the node and its sibling w is black, and both children of w is black,
    re-color w to red, in final we will recolor the node's parent to black
    Case 3: the node sibling w is black, w's left child is red, right child is black,
    switch the color of w and its left child, then perform right rotation, transform
    case 3 to case 4
    Case 4: the node sibling w is black, and its children are red
    
    Cases 1, 3, and 4 lead to termination after performing a constant number of color
    changes and at most three rotations. Case 2 is the only case in which the while loop
    can be repeated, and then the pointer node moves up the tree at most O(logn) times,
    performing no rotations.
    """

    def delete_fixup(self, node):
        while node != self.root and node.color == "B":
            if node == node.parent.left:
                w = node.parent.right
                if w.color == "R":
                    w.color = "B"
                    node.parent.color = "R"
                    self.left_rotate(node.parent)
                    w = node.parent.right
                if w.left.color == "B" and w.right.color == "B":
                    w.color = "R"
                    node = node.parent
                else:
                    if w.right.color == "B":
                        w.left.color = "B"
                        w.color = "R"
                        self.right_rotate(w)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = "B"
                    w.right.color = "B"
                    self.left_rotate(node.parent)
                    node = self.root
            elif node == node.parent.right:
                w = node.parent.left
                if w.color == "R":
                    w.color = "B"
                    node.parent.color = "R"
                    self.right_rotate(node.parent)
                    w = node.parent.left
                if w.right.color == "B" and w.left.color == "B":
                    w.color = "R"
                    node = node.parent
                else:
                    if w.left.color == "B":
                        w.right.color = "B"
                        w.color = "R"
                        self.left_rotate(w)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = "B"
                    w.left.color = "B"
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = "B"


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


bst = RBT()
test = [12, 5, 18, 2, 9, 15, 19, 17]
for i in test:
    bst.insert(i)
bst.traverse_in_order(bst.root)
bst.insert(13)
bst.traverse_in_order(bst.root)
