"""
Leet code 143: Reorder List
Techniques: Fast and Slow Pointer, Reverse Linked List, Two Pointers, Array
Complexity: O(n) where n is the number of nodes in the linked list
Space Complexity: O(1) for the in-place approach, O(n) for the array approach
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # fast and slow pointer, reverse second half, merge 2 lists in place
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    # array, 2 pointers, replace values
    def reorderList(self, head):
        arr, curr = [], head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        curr = head
        l, r = 0, len(arr) - 1
        while curr and curr.next:
            curr.val = arr[l]
            curr = curr.next
            l += 1
            curr.val = arr[r]
            curr = curr.next
            r -= 1
        if len(arr) % 2 == 1:
            curr.val = arr[l]
