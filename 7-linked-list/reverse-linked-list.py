"""
Leet code 206: Reverse Linked List
Techniques: iterative, two pointers
Time complexity: O(n)
Space complexity: O(1)
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
