"""
Problem: 169. Majority Element
Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Topic: Arrays & Hashing

---

Approach:
    Keep a candidate and a count. Its like each candidate voting for themselves.
    if same candidate appears then count is increased by 1 else count is decreased by 1.
    If count drops to 0, pick a new candidate.
    The majority element (appearing > n/2 times) will always survive.

    Example: nums = [2, 2, 1, 1, 1, 2, 2]
    - candidate=2, count: 1->2->1 ->0 -> candidate=1, count: 1->0 -> candidate=2, count: 1->2
    - Answer: 2  since candidate 2 was in lead

Time Complexity: O(n) 
Space Complexity: O(1) 
"""


class Solution:
    def cad(self,nums):
        count  = 0
        candidate = 0
        for num in nums:
            if count ==0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate