"""
You are given an array prices where prices[i] is the price of a given
stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.
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
