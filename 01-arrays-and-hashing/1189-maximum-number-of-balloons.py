"""
Problem: 1189. Maximum Number of Balloons
Link: https://leetcode.com/problems/maximum-number-of-balloons/
Difficulty: Easy
Topic: Arrays & Hashing

---

Approach:
    Count frequency of each character in the text.
    The word "balloon" needs: b=1, a=1, l=2, o=2, n=1.
    The answer is the minimum number of times we can form "balloon"
    based on available character counts.

    Example: text = "loonbalxballpoon"
    - Count: b=2, a=2, l=4, o=4, n=2 (and others)
    - b: 2/1=2, a: 2/1=2, l: 4/2=2, o: 4/2=2, n: 2/1=2
    - Answer: min(2,2,2,2,2) = 2

Time Complexity: O(n) - count characters
Space Complexity: O(1) - fixed size counter
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for c in text:
            count[c] = count.get(c, 0) + 1
        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )
