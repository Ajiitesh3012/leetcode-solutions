"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Topic: Arrays & Hashing

---

Approach:
    Count frequency of each number, then use bucket sort.
    Create buckets where index = frequency, value = list of numbers with that frequency.
    Iterate from highest frequency bucket to collect top k elements.

    Example: nums = [1,1,1,2,2,3], k = 2
    - Count: {1:3, 2:2, 3:1}
    - Buckets: [[], [3], [2], [1], [], [], []]
    - From right: bucket[3]=[1], bucket[2]=[2] → Answer: [1, 2]

Time Complexity: O(n) - counting + bucket sort
Space Complexity: O(n) - frequency map + buckets
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Bucket sort: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect top k from highest frequency
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
