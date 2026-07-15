"""
Problem: 15. 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium
Topic: Two Pointers

---

Approach:
    Sort the array. Fix one number, then use two pointers to find pairs
    that sum to the negative of the fixed number.
    Skip duplicates to avoid duplicate triplets.

    Example: nums = [-1, 0, 1, 2, -1, -4]
    - Sorted: [-4, -1, -1, 0, 1, 2]
    - Fix -1, find two numbers that sum to 1 → (0, 1) 
    - Fix -1 (skip duplicate)
    - Fix 0, find two that sum to 0 → none
    - Answer: [[-1, -1, 2], [-1, 0, 1]]

Time Complexity: O(n^2) - sort O(n log n) + nested loop O(n^2)
Space Complexity: O(1) - ignoring output space
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        empty = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            left = i + 1
            right = len(nums) - 1
            while left<right:
                total = nums[left] + nums[right] + nums[i]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    empty.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left - 1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return empty
