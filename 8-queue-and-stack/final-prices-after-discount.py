"""
Leet code 1475: Final Prices With a Special Discount in a Shop
Techniques: Monotonic Stack, Brute Force
Complexity: O(n) where n is the length of prices
Space Complexity: O(n) for the stack used in the monotonic stack approach
"""


class Solution(object):
    # monotonic stack
    def finalPrices(self, prices):
        s = []
        for i in range(len(prices) - 1, -1, -1):
            while s and prices[i] < s[-1]:
                s.pop()
            s.append(prices[i])
            prices[i] = prices[i] - s[-2] if len(s) > 1 else prices[i]
        return prices

    # brute force
    def finalPrices(self, prices):
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)
        return answer
