var nextGreaterElement = function(nums1, nums2) {
    let stack = []
    let hashMap = {}
    for (let i = nums2.length-1; i>=0; i--) {
        while (stack.length && nums2[i] > stack.at(-1)) stack.pop()
        hashMap[nums2[i]] = stack.length > 0 ? stack.at(-1) : -1
        stack.push(nums2[i])
    }
    for (let i = 0; i < nums1.length; i++) nums1[i] = hashMap[nums1[i]]
    return nums1
};