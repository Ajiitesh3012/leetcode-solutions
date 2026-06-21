"""
Problem: 1732. Find the Highest Altitude
Link: https://leetcode.com/problems/find-the-highest-altitude/
Difficulty: Easy
Topic: Arrays & Hashing (Prefix Sum)

---

Approach:
    Start at altitude 0. The gain array tells us the net change
    between consecutive points. Track the running altitude and
    keep the maximum seen.

    Example: gain = [-5, 1, 5, 0, -7]
    - Altitudes: 0, -5, -4, 1, 1, -6
    - Highest = 1 

Time Complexity: O(n) 
Space Complexity: O(n) 
"""


class Solution:
    def largestAltitude(self, gain):
        list1 = []
        list1.append(0)
        for num in gain:
            list1.append(num)
        s = 0
        list2 =[]
        for i in range(0,len(list1)):
            s+=list1[i]
            list2.append(s)
        return (max(list2))
