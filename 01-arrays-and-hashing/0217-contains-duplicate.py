"""
Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topic: Arrays & Hashing

---

Approach:
    Use a set to track numbers we've seen.
    If a number is already in the set, it's a duplicate.

    Example: nums = [1, 2, 3, 1]
    - num=1, not in set -> add {1}
    - num=2, not in set -> add {1, 2}
    - num=3, not in set -> add {1, 2, 3}
    - num=1, already in set -> return True 

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - set stores at most n elements
"""


class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
