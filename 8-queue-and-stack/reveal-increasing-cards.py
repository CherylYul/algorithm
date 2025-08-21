"""
Leet code 950: Reveal Cards In Increasing Order
Techniques: Queue Simulation
Complexity: O(n log n) where n is the number of cards in the deck
Space Complexity: O(n) for the queue used to simulate the deck
"""

from collections import deque


class Solution(object):
    # brute force
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        q = deque(range(len(deck)))
        res = [None] * len(deck)
        for num in deck:
            i = q.popleft()
            res[i] = num
            if q:
                q.append(q.popleft())
        return res

    # queue simulation
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        if len(deck) <= 2:
            return deck
        res = [deck[-2], deck[-1]]
        for i in range(len(deck) - 3, -1, -1):
            res = [deck[i], res[-1]] + res[:-1]
        return res
