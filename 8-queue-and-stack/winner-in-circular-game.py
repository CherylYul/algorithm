"""
Leet code 1823: Find the Winner of the Circular Game
Techniques: Queue Simulation, Josephus Problem, Recursion, Iterative
Complexity: O(nk) for the queue simulation, O(n) for recursion, and iterative approaches
Space Complexity: O(n) for the queue simulation, and recursion, O(1) for iterative approach
"""

from collections import deque


class Solution(object):
    # Iterative, Josephus Problem
    def findTheWinner(self, n, k):
        pos = 0
        for l in range(n - 1):
            pos = (pos + k) % (l + 2)
        return pos + 1

    # Recursion, Josephus Problem
    def findTheWinner(self, n, k):
        def recursive(n, k):
            if n == 1:
                return 0
            return ((recursive(n - 1, k)) + k) % n

        return recursive(n, k) + 1

    # Queue Simulation more efficiently
    def findTheWinner(self, n, k):
        q = deque(range(n))
        i = -1
        while i != len(q) - 1:
            for _ in range(k - 1):
                i += 1
                q.append(q[i])
            i += 1
        return q[i] + 1

    # Queue Simulation
    def findTheWinner(self, n, k):
        q = deque(range(n))
        while len(q) > 1:
            count = k - 1
            while count:
                q.append(q.popleft())
                count -= 1
            q.popleft()
        return q[0] + 1
