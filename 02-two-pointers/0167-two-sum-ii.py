"""
Problem: 167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Topic: Two Pointers

---

Approach:
    Since the array is sorted, use two pointers at both ends.
    If sum<target, move left pointer right(left+=1) ->(increase sum).
    If sum>target, move right pointer left(right-=1) ->(decrease sum).

    Example: numbers = [2, 7, 11, 15], target = 9
   

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - no extra space
"""


class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return (left + 1, right + 1)
            elif current_sum <= target:
                left+=1
            else:
                right-=1
sol = Solution()
numbers = [2,4,6,9,10]
target = 8
result= sol.twoSum(numbers,target)
print(result)