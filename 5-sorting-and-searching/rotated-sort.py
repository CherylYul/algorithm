class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        pivot = n - 1
        if nums[pivot] == target:
            return pivot
        if nums[pivot] < target:
            for i in range(0, n - 1):
                if nums[i] == target:
                    return i
                if nums[i + 1] < nums[i]:
                    return -1
        for i in range(n - 2, -1, -1):
            if nums[i] == target:
                return i
            if nums[i - 1] > nums[i]:
                return -1
        return -1

    def search2(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
