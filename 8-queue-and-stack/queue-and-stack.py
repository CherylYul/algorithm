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


"""
Implement a queue using two stacks. Leetcode 232.
Time complexity: O(1) for push, O(n) for pop and peek.
Space complexity: O(n) for the two stacks.
"""


class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
