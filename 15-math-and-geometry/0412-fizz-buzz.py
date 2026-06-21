"""
Problem: 412. Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/
Difficulty: Easy
Topic: Math & Geometry

---

Approach:
    Iterate from 1 to n. Check divisibility:
    - Divisible by 15 (both 3 and 5) → "FizzBuzz"
    - Divisible by 3 only → "Fizz"
    - Divisible by 5 only → "Buzz"
    - Otherwise → the number as string

    Check 15 first to avoid printing just "Fizz" or "Buzz" for multiples of both.

Time Complexity: O(n) - iterate through all numbers
Space Complexity: O(n) - output list stores n elements
"""


class Solution:
    def fizzBuzz(self, n):
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result
