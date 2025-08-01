/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    const n = nums.length
    let prefix = 1
    let suffix = 1
    let best = -Infinity
    for (let i=0; i<n; i++) {
        prefix *= nums[i]
        suffix *= nums[n-1-i]
        best = Math.max(prefix, suffix, best)
        if (prefix === 0) prefix = 1
        if (suffix === 0) suffix = 1
    }
    return best
};