"""
You are given an array prices where prices[i] is the price of a given
stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.
Solution: sliding window
O(n) time complexity
O(1) space complexity
"""


class Solution(object):
    def maxProfit(self, prices):
        l, best_profit = 0, 0
        for curr in range(1, len(prices)):
            if prices[curr] < prices[l]:
                l = curr
                continue
            profit = prices[curr] - prices[l]
            best_profit = max(profit, best_profit)
        return best_profit

    def maxProfit2(self, prices):
        l, best = 0, 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[l]
            if profit > best:
                best = profit
            if profit < 0:
                l = i
        return best


"""
1. only move pointer l when the profit is negative, which means there is a lower price to buy
2. otherwise, just keep the pointer, since the best profit is always saved in best
"""
