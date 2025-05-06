"""
Design a circular queue with the following operations:
- `MyCircularQueue(k)`: Initializes the queue with a size of `k`.
- `enQueue(value)`: Adds an item to the rear of the queue. Returns `true` if the operation is successful.
- `deQueue()`: Removes an item from the front of the queue. Returns `true` if the operation is successful.
- `Front()`: Gets the front item from the queue. Returns `-1` if the queue is empty.
- `Rear()`: Gets the last item from the queue. Returns `-1` if the queue is empty.
- `isEmpty()`: Checks whether the circular queue is empty or not.
- `isFull()`: Checks whether the circular queue is full or not.
- `MyCircularQueue` is a class that implements a circular queue.
"""


class MyCircularQueue(object):
    def __init__(self, k):
        self.size = k
        self.head = 0
        self.nums = 0
        self.queue = [None] * k

    def enQueue(self, value):
        if self.isFull():
            return False
        idx = (self.head + self.nums) % self.size
        self.queue[idx] = value
        self.nums += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.nums -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        idx = (self.head + self.nums - 1) % self.size
        return self.queue[idx]

    def isEmpty(self):
        return self.nums == 0

    def isFull(self):
        return self.nums == self.size
