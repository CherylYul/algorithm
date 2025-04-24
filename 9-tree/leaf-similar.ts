/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function (root1, root2) {
  const dfs = (root) => {
    if (!root) return [];
    const leaves = dfs(root.left).concat(dfs(root.right));
    return leaves.length > 0 ? leaves : [root.val];
  };
  return JSON.stringify(dfs(root1)) === JSON.stringify(dfs(root2));
};
