"""
Problem: 2469. Convert the Temperature
Link: https://leetcode.com/problems/convert-the-temperature/
Difficulty: Easy
Topic: Math & Geometry

---

Approach:
    Apply conversion formulas:
    - Kelvin = Celsius + 273.15
    - Fahrenheit = Celsius * 1.80 + 32.00

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]
