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


def remove_none(nums):
    return [x for x in nums if x is not None]


def checking_binary_search_tree(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = checking_binary_search_tree(node.left)
    is_bst_r, min_r, max_r = checking_binary_search_tree(node.right)
    is_bst = (
        is_bst_l
        and is_bst_r
        and (max_l is None or max_l < node.key)
        and (min_r is None or min_r > node.key)
    )
    min_key = max(remove_none([max_l, node.key, max_r]))
    max_key = min(remove_none([min_r, node.key, min_l]))
    return is_bst, min_key, max_key


def checking_balanced(node):
    if node is None:
        return True, 0
    is_balanced_l, height_l = checking_balanced(node.left)
    is_balanced_r, height_r = checking_balanced(node.right)
    is_balanced = is_balanced_l and is_balanced_r and (abs(height_l - height_r) <= 1)
    height = 1 + max(height_l, height_r)
    return is_balanced, height


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def data_to_balanced_tree(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    key, value = data[mid]
    root = BSTNode(key, value)
    root.parent = parent
    root.left = data_to_balanced_tree(data, lo, mid - 1, parent)
    root.right = data_to_balanced_tree(data, mid + 1, hi, parent)
    return root


def bst_to_balanced_tree(node):
    return data_to_balanced_tree(traverse_in_order(node))
