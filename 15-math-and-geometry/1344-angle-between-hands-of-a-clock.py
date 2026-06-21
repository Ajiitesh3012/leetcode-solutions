"""
Problem: 1344. Angle Between Hands of a Clock
Link: https://leetcode.com/problems/angle-between-hands-of-a-clock/
Difficulty: Medium
Topic: Math & Geometry

---

Approach:
    Calculate the angle of each hand from 12 o'clock position:
    - Minute hand: minutes * 6 degrees (360/60 = 6 per minute)
    - Hour hand: (hour % 12) * 30 + minutes * 0.5 degrees
      (30 per hour + 0.5 per minute as hour hand moves gradually)
    - Return the smaller of the two possible angles.

    Example: hour = 3, minutes = 30
    - Minute angle = 30 * 6 = 180°
    - Hour angle = 3 * 30 + 30 * 0.5 = 105°
    - Diff = |180 - 105| = 75° 

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def angleClock(self, hour, minutes):
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)
