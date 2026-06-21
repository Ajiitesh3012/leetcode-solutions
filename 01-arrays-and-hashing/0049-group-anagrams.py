"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topic: Arrays & Hashing

---

Approach:
    Use a hashmap where the key is the sorted version of each string.
    All anagrams will have the same sorted key, so they group together.

    Example: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    - sorted("eat") = "aet" → group: [eat, tea, ate]
    - sorted("tan") = "ant" → group: [tan, nat]
    - sorted("bat") = "abt" → group: [bat]

Time Complexity: O(n * k log k) - n strings, each sorted in k log k
Space Complexity: O(n * k) - storing all strings in hashmap
"""


class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            sorted_key = ''.join(sorted(word))
            if sorted_key not in groups:
                groups[sorted_key] = []
            groups[sorted_key].append(word)

        return list(groups.values())
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = sol.groupAnagrams(strs)
print(result)
