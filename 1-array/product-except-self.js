/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const res = new Array(nums.length).fill(1)
    for (let i=1; i<nums.length; i++) {
        res[i] = nums[i-1] * res[i-1]
    }
    suffix = 1
    for (let i=nums.length-2; i>-1; i--) {
        suffix *= nums[i+1]
        res[i] *= suffix
    }
    return res
};