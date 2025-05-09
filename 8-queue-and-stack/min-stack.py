"""
LeetCode 155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Time complexity: O(1) for all operations
Space complexity: O(n)
"""


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minPos = [0]

    def push(self, val):
        self.stack.append(val)
        if val < self.stack[self.minPos[-1]]:
            self.minPos.append(len(self.stack) - 1)

    def pop(self):
        if self.minPos[-1] == len(self.stack) - 1 and self.minPos[-1] != 0:
            self.minPos.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack[self.minPos[-1]]
