"""
Leet code 977: Squares of a Sorted Array
Techniques: two pointers, sorting, stack
Complexity: O(n) for two pointers and stack, O(n log n) for sorting
Space Complexity: O(n) for stack and result array, O(1) for sorting in place
"""


class Solution(object):
    # two pointers
    def sortedSquares(self, nums):
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
        return res

    # sorting
    def sortedSquares(self, nums):
        if len(nums) == 1:
            return [nums[0] ** 2]
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums

    # stack
    def sortedSquares(self, nums):
        stack, res = [], []
        for num in nums:
            if num < 0:
                stack.append(-num)
            else:
                while stack and stack[-1] < num:
                    res.append(stack.pop() ** 2)
                res.append(num**2)
        while stack:
            res.append(stack.pop() ** 2)
        return res
