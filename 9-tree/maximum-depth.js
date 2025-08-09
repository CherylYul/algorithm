function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

var maxDepth = function(root) {
    if (!root) return 0
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1
};

var maxDepth = function(root) {
    if (!root) return 0
    let q = []
    let depth = 0
    q.push(root)
    while (q.length) {
        depth++;
        let n = q.length
        for (let i=0; i<n; i++){
            let node = q.shift()
            if (node.left) q.push(node.left)
            if (node.right) q.push(node.right)
        }
    }
    return depth
};