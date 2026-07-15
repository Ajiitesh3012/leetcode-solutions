"""
Problem: 121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Topic: Sliding Window

---

Approach:
    Track the minimum price seen so far and the maximum profit.
    For each day, calculate profit if we sell today (price - min_price).
    Update max_profit if this profit is better.

    Example: prices = [7, 1, 5, 3, 6, 4]
    - min=7, profit=0
    - min=1, profit=0
    - min=1, profit=4 (5-1)
    - min=1, profit=4
    - min=1, profit=5 (6-1) ← answer
    - min=1, profit=5

Time Complexity: O(n) - single pass
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
