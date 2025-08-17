/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
  let isIncrease = false
  let isDecrease = false
  for (let i=1; i<nums.length; i++) {
    if (nums[i] < nums[i-1]) isDecrease = true
    if (nums[i] > nums[i-1]) isIncrease = true
    if (isIncrease && isDecrease) return false
  }
  return true
};