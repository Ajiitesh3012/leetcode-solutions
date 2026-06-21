"""
Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topic: Arrays & Hashing

---

Approach:
    Count frequency of each character in both strings using a hashmap.
    Increment for string s, decrement for string t.
    If any count goes negative, t has extra characters → not an anagram.

    Example: s = "anagram", t = "nagaram"
    - Both have: a=3, n=1, g=1, r=1, m=1 → True 

Time Complexity: O(n)
Space Complexity: O(1) 
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get[char,0] + 1
        for char in t:
            if char not in count:
                return False
            
            count[char]-=1
            if count[char]<0:
                return False
        return True