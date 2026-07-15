"""
Problem: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Topic: Two Pointers

---

Approach:
    Use two pointers at both ends. Calculate area = min(height[l], height[r]) * (r - l).
    Move the pointer with the shorter height inward.

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        water = set()
        maxStored = 0
        right = len(height) - 1
        left = 0
        while left<right:
            current = (right - left) * min(height[left], height[right])
            maxStored = max(maxStored,current)
            if height[left]<height[right]:
                left+=1
            else: right-=1
        return maxStored

