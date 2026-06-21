"""
Problem: 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Topic: Math & Geometry

---

Approach:
    Convert the number to a string and check if it reads the same forwards and backwards. 

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
sol = Solution()

