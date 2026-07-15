"""
Problem: 739. Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium
Topic: Stack

---

Approach:
    Use a stack that stores indices.
    For each temperature, pop all smaller temperatures from the stack
    and calculate the number of days waited.

    Example: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    - 73: push → stack: [0]
    - 74 > 73: pop 0, days[0]=1 → stack: [1]
    - 75 > 74: pop 1, days[1]=1 → stack: [2]
    - 71 < 75: push → stack: [2, 3]
    - 69 < 71: push → stack: [2, 3, 4]
    - 72 > 69,71: pop 4 days[4]=1, pop 3 days[3]=2 → stack: [2, 5]
    - 76 > 72,75: pop... → Answer: [1,1,4,2,1,1,0,0]

Time Complexity: O(n) - each index pushed and popped at most once
Space Complexity: O(n) - stack
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i-prev
            stack.append(i)

        return result
