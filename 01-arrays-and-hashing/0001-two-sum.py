"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Arrays & Hashing

---

Description:
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

Approach:
    Using a hashmap to store numbers we've already seen.
    For each number, check if (target - current number) exists in the map.
    If yes, we found our pair. If no, store current number and continue.

    Example: nums = [2, 7, 11, 15], target = 9
    - i=0: num=2, need 9-2=7. 7 not in map hence store {2: 0}
    - i=1: num=7, need 9-7=2, 2 IS in map at index 0 hence return [0, 1] because 
      0 is index of 2 stored in seen and 1 is index of 7 in nums.

Time Complexity: O(n) 
Space Complexity: O(n) 
"""


class Solution():
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]=i
        return 0            

obj = Solution()
nums = [2,7,11,15]
target = 9
x = obj.twoSum(nums,target)
print (x)
