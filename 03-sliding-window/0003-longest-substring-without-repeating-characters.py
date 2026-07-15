"""
Problem: 3. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Topic: Sliding Window

---

Approach:
    Use a sliding window with a set to track characters in current window.
    Expand right pointer to include new characters.
    If duplicate found, shrink from left until no duplicates.


Time Complexity: O(n) - each character visited at most twice
Space Complexity: O(min(n, 26)) - set of characters in window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left += 1

            store.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
