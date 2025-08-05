"""
Leet code 141: Linked List Cycle
Techniques: fast slow pointers (Floyd's cycle detection)
Time complexity: O(n)
Space complexity: O(1)
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
