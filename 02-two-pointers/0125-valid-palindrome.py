"""
Problem: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topic: Two Pointers

---

Approach:
    Use two pointers from both ends. Skip non-alphanumeric characters.
    Compare characters (case-insensitive) moving inward.

    Example: s = "A man, a plan, a canal: Panama"
    - After filtering: "amanaplanacanalpanama"
    - Left pointer →  Right pointer ← both match → True 

Time Complexity: O(n) 
Space Complexity: O(n) 
"""


class Solution:
    def isPalindrome(self, s):
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        return ( s == s[::-1])