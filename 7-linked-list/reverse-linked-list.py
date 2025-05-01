"""
Solution: two pointers
Time Complexity: O(N)
Space Complexity: O(1)
"""


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
