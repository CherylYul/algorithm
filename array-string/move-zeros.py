"""
The problem requires moving all zeros in the array to the end while
maintaining the relative order of the non-zero elements. The simplest
way to achieve this is to use a two-pointer technique. One pointer
(nonzero) tracks the position for the next non-zero number, while the
other pointer (i) traverses the array.
1. Use two pointers:
   nonzero: Keeps track of the index to place the next non-zero element.
   i: Iterates through the array.
2. Traverse the array:
   If the current element is non-zero, swap it with the element at the
   nonzero pointer and increment the nonzero pointer. Move the i pointer forward.
3. At the end of the traversal, all zeros will be shifted to the right, and
   the relative order of non-zero elements will be preserved.
>> move numbers to the front of the array, keep track of two pointers
"""


class Solution(object):
    def moveZeroes(self, nums):
        non_zeros, i = 0, 0
        length = len(nums)
        while i < length:
            if nums[i] != 0:
                nums[i], nums[non_zeros] = nums[non_zeros], nums[i]
                non_zeros += 1
            i += 1
        return nums
