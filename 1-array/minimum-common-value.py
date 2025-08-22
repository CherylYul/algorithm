"""
Leet code 2540: Minimum Common Value
Techniques: Two Pointers, Hash Set, Binary Search
Complexity: O(n + m) two pointers and hash set, O(n log m) binary search
Space Complexity: O(1) two pointers, O(n) hash set and binary search
"""


class Solution(object):
    # Hash Set
    def getCommon(self, nums1, nums2):
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                return num
        return -1

    # Two Pointers
    def getCommon(self, nums1, nums2):
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1
        n1, n2 = 0, 0
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                return nums1[n1]
            if nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        return -1

    # Binary Search
    def getCommon(self, nums1, nums2):
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1

        def search(target):
            l, r = 0, len(nums1) - 1
            while l <= r:
                mid = (l + r) / 2
                if nums1[mid] == target:
                    return True
                if target < nums1[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        for num in nums2:
            if search(num):
                return num
        return -1
