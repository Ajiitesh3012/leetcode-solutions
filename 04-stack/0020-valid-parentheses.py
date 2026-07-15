"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Topic: Stack

---

Approach:
    Use a stack. Push opening brackets onto the stack.
    When a closing bracket appears, check if it matches the top of the stack.
    If stack is empty at the end, all brackets are matched.

    Example: s = "({[]})"
    - '(' → push → stack: ['(']
    - '{' → push → stack: ['(', '{']
    - '[' → push → stack: ['(', '{', '[']
    - ']' → matches '[' → pop → stack: ['(', '{']
    - '}' → matches '{' → pop → stack: ['(']
    - ')' → matches '(' → pop → stack: []
    - Stack empty → True 

Time Complexity: O(n) - single pass
Space Complexity: O(n) - stack
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack ={")":"(","]":"[", "}":"{"}
        steck = []
        for ch in s:
            if ch in "([{":
                steck.append(ch)
            else:
                if not steck:
                    return False        
                elif steck[-1]!=stack[ch]:
                    return False
                steck.pop()    
        return len(steck) == 0
