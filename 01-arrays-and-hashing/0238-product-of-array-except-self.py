"""
Problem: 238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Topic: Arrays & Hashing

---

Approach:
    Two passes — no division allowed.
    Pass 1 (left to right): store running product of everything to the LEFT.
    Pass 2 (right to left): multiply by running product of everything to the RIGHT.

    Example: nums = [1, 2, 3, 4]
    - Left products:  [1, 1, 2, 6]
    - Right products: [24, 12, 4, 1]
    - Result:         [24, 12, 8, 6]

Time Complexity: O(n)
Space Complexity: O(1) 
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n

        left_product = 1
        for i in range(n):
            result[i]=left_product
            left_product*=nums[i]

        right_product=1
        for i in range(n-1,-1,-1):
            result[i]*=right_product
            right_product*=nums[i]

        return result
