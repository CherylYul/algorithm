"""
Leet code 2073: Time Needed to Buy Tickets
Techniques: Queue Simulation, Mathematical Calculation
Complexity: O(n) where n is the number of tickets in the queue
Space Complexity: O(n) for the queue used to simulate the ticket buying process
"""

from collections import deque


class Solution(object):
    # Mathematical Calculation
    def timeRequiredToBuy(self, tickets, k):
        time = tickets[k] * len(tickets)
        for i in range(len(tickets)):
            curr = tickets[i] - tickets[k]
            if i < k and curr < 0:
                time += curr
            if i > k and curr < -1:
                time += curr + 1
        return time - (len(tickets) - k - 1)

    # Queue Simulation
    def timeRequiredToBuy(self, tickets, k):
        if len(tickets) == 1:
            return tickets[0]
        q = deque(range(len(tickets)))
        time = 0
        while q:
            i = q.popleft()
            tickets[i] -= 1
            time += 1
            if tickets[i] == 0 and k == i:
                return time
            if tickets[i] > 0:
                q.append(i)
        return time
