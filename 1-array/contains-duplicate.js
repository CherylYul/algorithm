/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const mySet = new Set();
    for (const num of nums) {
        if (mySet.has(num)) return true;
        mySet.add(num);
    }
    return false;
};