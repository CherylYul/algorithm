"""
Leet Code 23: Merge k Sorted Lists
Techniques: linked list manipulation, divide and conquer, hash map, merge sort
Time complexity: O(n log k), where n is the total number of nodes across all lists and k is the number of lists
Space complexity: O(k), for storing the lists in the merge process
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    # def mergeKLists(self, lists):
    #     hash_map = {}
    #     for i in range(len(lists)):
    #         curr = lists[i]
    #         while curr:
    #             hash_map[curr.val] = hash_map.get(curr.val, 0) + 1
    #             curr = curr.next
    #     sorted_hash_map = sorted(hash_map.keys())
    #     dummy = ListNode(-1)
    #     curr = dummy
    #     for i in sorted_hash_map:
    #         for _ in range(hash_map[i]):
    #             curr.next = ListNode(i)
    #             curr = curr.next
    #     return dummy.next
