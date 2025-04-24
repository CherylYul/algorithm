/**
 * @param {TreeNode} root
 * @return {number}
 */

// DFS: recursion
// Time complexity: O(n)
// Space complexity: O(h), where h is the height of the tree
var maxDepth = function (root) {
  if (!root) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};

// BFS: queue
// Time complexity: O(n)
// Space complexity: O(n)
// var maxDepth = function(root) {
//     if (!root) return 0;
//     const queue = []
//     queue.push(root)
//     let depth = 0
//     while (queue.length) {
//         depth++;
//         const size = queue.length
//         for(let i=0; i<size; i++){
//             const node = queue.shift()
//             if (node.left) queue.push(node.left)
//             if (node.right) queue.push(node.right)
//         }
//     }
//     return depth
// };
