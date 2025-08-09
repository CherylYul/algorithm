function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (!root) return root;
    let temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.left)
    invertTree(root.right)
    return root
};

var invertTree = function(root) {
    if (!root) return root;
    let q = [root]
    while (q.length) {
        let node = q.shift()
        let temp = node.right
        node.right = node.left
        node.left = temp
        if (node.right) q.push(node.right)
        if (node.left) q.push(node.left)
    }
    return root;
};