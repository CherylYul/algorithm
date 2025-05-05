"""
Implement a stack using two queues. Leetcode 225.
Time complexity: O(n) for pop and top, O(1) for push.
Space complexity: O(n) for the two queues.
"""


class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        value = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return value

    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        value = self.q1[0]
        self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        return value

    def empty(self):
        return len(self.q1) == 0
