"""
Problem: 1833. Maximum Ice Cream Bars
Link: https://leetcode.com/problems/maximum-ice-cream-bars/
Difficulty: Medium
Topic: Greedy

---

Approach:
    Sort costs in ascending order. Buy the cheapest ice cream bars first
    until we run out of coins. This greedy approach maximizes the count.

    Example: costs = [1, 3, 2, 4, 1], coins = 7
    - Sorted: [1, 1, 2, 3, 4]
    - Buy 1 (coins=6), buy 1 (coins=5), buy 2 (coins=3), buy 3 (coins=0)
    - Can't afford 4 → Answer: 4

Time Complexity: O(n log n) - sorting
Space Complexity: O(1) - in-place sort
"""


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break

        return count
