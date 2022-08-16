class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def tuple_to_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = tuple_to_tree(data[0])
        node.right = tuple_to_tree(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))
    if node is None:
        return None


def display_tree(node, space="\t", height=0):
    if node is None:
        print(space * height, "x")
        return
    if node.left == None and node.right == None:
        print(space * height, node.key)
        return
    display_tree(node.left, space, height + 1)
    print(space * height, node.key)
    display_tree(node.right, space, height + 1)


def traverse_in_order(node):
    if node is None:
        return None
    return (
        traverse_in_order(node.left),
        print(node.key, end=" "),
        traverse_in_order(node.right),
    )


def traverse_pre_order(node):
    if node is None:
        return None
    return (
        print(node.key, end=" "),
        traverse_pre_order(node.left),
        traverse_pre_order(node.right),
    )


def traverse_post_order(node):
    if node is None:
        return None
    return (
        traverse_post_order(node.left),
        traverse_post_order(node.right),
        print(node.key, end=" "),
    )


def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))


def calculate_size(node):
    if node is None:
        return 0
    return 1 + calculate_size(node.left) + calculate_size(node.right)
