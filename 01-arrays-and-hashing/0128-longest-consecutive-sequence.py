"""
Problem: 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Topic: Arrays & Hashing

---

Approach:
    Put all numbers in a set. For each number, check if it's the START
    of a sequence (i.e., num-1 is NOT in the set). If yes, count how
    far the sequence goes (num+1, num+2, ...).

    Example: nums = [100, 4, 200, 1, 3, 2]
    - 100: start of seq -> 100 -1 = 99 not in set, length = 1 but num + 1 = 101 not in set
    - 4: not a start (because 3 exists)
    - 200: start of seq -> 200 (length = 1, and num + 1 = 201 not in set)
    - 1: start of seq -> 1,2,3,4 (length 4) 
    - Answer: 4

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1

                while num + length in num_set:
                    length += 1

                longest = max(longest, length)

        return longest
